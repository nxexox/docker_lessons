import os
from flask import Flask, request, abort, jsonify
from flask_mail import Mail, Message


MAIL_SERVER = os.getenv('SMTP_HOST', 'postfix')
MAIL_PORT = os.getenv('SMTP_PORT', 25)
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = os.getenv('SMTP_USER', 'user')
MAIL_PASSWORD = os.getenv('SMTP_PASSWORD', 'password')
MAIL_DEFAULT_SENDER = 'user@gmail.com'

app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)


@app.route('/', methods=['post'])
def send_mail():
    if request.method == 'POST' and request.is_json:
        mail_to = request.json.get('email')
        mail_head, mail_ms = request.json.get('title'), request.json.get('text', 'Hello')
        if any((not mail_to, not mail_head, not mail_ms)):
            abort(400)
        msg = Message(mail_head, sender='user@gmail.com', recipients=[mail_to])
        msg.body = mail_ms
        mail.send(msg)
        return jsonify(message='Сообщение успешно отправлено')

    abort(405)


@app.errorhandler(405)
def handler_405(e):
    return jsonify(error=405, message='Неверный запрос'), 405


@app.errorhandler(400)
def handler_400(e):
    return jsonify(error=400, message='Не корректые данные')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('EMAIL_BACKEND_PORT', 5000))
