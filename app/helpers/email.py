from flask_mail import Message

from app.utils import mail


def send_email(email: str, template: str = '', **kwargs):
    if not template:
        raise Exception('Template is required')

    if template == 'contact':
        msg = Message('New contact request', recipients=['recipient@example.com'])
        msg.body = f'New contact request from {kwargs.get("name") or "Anonim"} {kwargs.get("surname") or "Anonim"} with message:\n{kwargs.get("message")}'

        try:
            mail.send(msg)
        except Exception as e:
            return {'status': False, 'message': str(e)}
    elif template == 'newsletter':
        msg = Message('New newsletter request', recipients=['recipient@example.com'])
        msg.body = f'New newsletter request'

        try:
            mail.send(msg)
        except Exception as e:
            return {'status': False, 'message': str(e)}

    return {'status': True}
