__author__ = 'eric'

from threading import Thread
from flask import render_template, current_app
from flask_mail import Message
from app import mail


def async_email(app, msg):
    with app.app_context():
        return mail.send(msg)


def sync_email(app, msg):
    with app.app_context():
        return mail.send(msg)


def send_async_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return async_email(app, msg)


def send_sync_email(to, subject, template, **kwargs):
    try:
        app = current_app._get_current_object()
        msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                      sender=app.config['MAIL_SENDER'], recipients=to)
        msg.html = render_template(template + '.html', **kwargs)
        sync_email(app, msg)
        return True
    except:
        return False
