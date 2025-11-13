"""Integration with n8n workflow automation platform."""

import requests
import json
import os
from datetime import datetime, timedelta

N8N_WEBHOOK_URL = os.getenv('N8N_WEBHOOK_URL', 'https://amrmohamedz0.app.n8n.cloud/webhook-test/ai-booking')
N8N_AUTH_HEADER = os.getenv('N8N_AUTH_HEADER')
N8N_AUTH_VALUE = os.getenv('N8N_AUTH_VALUE')

def n8n_create_calendar_event(appointment):
    """Send appointment to n8n workflow for calendar sync and conflict detection."""
    try:
        date_str = appointment.get('date')
        time_str = appointment.get('time')
        duration = appointment.get('duration', 60)
        
        try:
            start_dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
            end_dt = start_dt + timedelta(minutes=duration)
        except Exception:
            start_dt = datetime.now()
            end_dt = start_dt + timedelta(minutes=duration)
        
        start_iso = start_dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        end_iso = end_dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        
        appointment_obj = {
            "title": appointment.get('title', 'Appointment'),
            "date": date_str,
            "time": time_str,
            "duration": duration,
            "start": start_iso,
            "end": end_iso,
            "startISO": start_iso,
            "endISO": end_iso,
            "description": appointment.get('description', 'Created via Voice Agent'),
            "location": appointment.get('location', ''),
            "participants": appointment.get('participants', [])
        }
        
        payload = {
            "action": "create_calendar_event",
            "appointment": appointment_obj,
            **appointment_obj
        }

        headers = {'Content-Type': 'application/json'}
        if N8N_AUTH_HEADER and N8N_AUTH_VALUE:
            headers[N8N_AUTH_HEADER] = N8N_AUTH_VALUE
        
        response = requests.post(
            N8N_WEBHOOK_URL,
            json=payload,
            headers=headers,
            timeout=30
        )
        
        if response.status_code == 200:
            try:
                result = response.json()
                
                if result.get('success'):
                    return {
                        'success': True,
                        'conflict': False,
                        'event_id': result.get('event_id') or result.get('eventId'),
                        'html_link': result.get('html_link') or result.get('htmlLink'),
                        'message': result.get('message', 'Event created successfully')
                    }
                elif result.get('conflict'):
                    return {
                        'success': False,
                        'conflict': True,
                        'alternatives': result.get('alternatives', []),
                        'message': result.get('message', 'Time conflict detected')
                    }
                else:
                    return {
                        'success': False,
                        'conflict': False,
                        'error': result.get('error', 'Workflow error'),
                        'message': result.get('message', 'Failed to create event')
                    }
            except json.JSONDecodeError:
                return {
                    'success': True,
                    'conflict': False,
                    'message': 'Event sent to workflow successfully'
                }
        else:
            return {
                'success': False,
                'conflict': False,
                'error': f'Workflow returned status {response.status_code}',
                'message': response.text or 'Workflow error'
            }
    except requests.exceptions.Timeout:
        return {
            'success': False,
            'conflict': False,
            'error': 'Workflow timeout',
            'message': 'Request took too long. Please try again.'
        }
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'conflict': False,
            'error': str(e),
            'message': f'Failed to connect to workflow: {str(e)}'
        }
    except Exception as e:
        return {
            'success': False,
            'conflict': False,
            'error': str(e),
            'message': f'Error: {str(e)}'
        }


def sync_calendar(appointment):
    """Alias for backward compatibility."""
    return n8n_create_calendar_event(appointment)

