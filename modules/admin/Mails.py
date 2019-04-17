from flask import Flask,jsonify
from flask_mail import Mail, Message
app = Flask(__name__)


mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'iamsachinjose@gmail.com',
    "MAIL_PASSWORD": 'gmail12345'
}

app.config.update(mail_settings)


def sendmail(title,body,receiver):
    mail = Mail(app)
    receivers=[]
    receivers.append(receiver)
    msg = Message(title, sender = 'SOCIAL MEDIA', recipients = receivers)
    msg.body = body
    mail.send(msg)
    return jsonify({
       "status":"success"
    })

