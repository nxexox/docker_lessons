import os
import socket
from flask import Flask

app = Flask(__name__)


name = os.getenv('USER_NAME', 'Неизвестный')
host = socket.gethostname()


@app.route('/')
def hello_world():
    return '''
        <!doctype html>
        <title>Главная страница</title>
        <h1>Привет: {}. Вы находитесь на {} сервере.</h1>
        <ul>
        <li><a href="/hello-by-name?name=Неизвестный">Приветствие по имени</a></li>
        </ul>
        '''.format(name, host)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
