import os

from flask import Flask, request, abort, Response
import requests

app = Flask(__name__)


BACKEND_URL = os.getenv('BACKEND_URL', 'http://0.0.0.0:5001')
if not BACKEND_URL:
    raise ValueError('Environ `BACKEND_URL` not found in system. Please check environment settings.')


@app.route('/')
def hello_world():
    return '''
        <!doctype html>
        <title>Главная страница</title>
        <h1>Что умеет ваше приложение:</h1>
        <ul>
        <li><a href="/hello-by-name?name=Неизвестный">Приветствие по имени</a></li>
        <li><a href="/calculate">Калькулятор</a></li>
        <li><a href="/jobs/list">Список запросов от JOB</a></li>
        </ul>
        '''


@app.route('/hello-by-name', methods=['get'])
def hello_by_name():
    name = request.args.get('name', None)
    if not name:
        bad_response_text = '''
        <!doctype html>
        <title>Ошибка! Пожалуйста введите имя!</title>
        <h1 style="color: red">Пожалуйста введите имя</h1>
        <form method=get>
          <label>Ваше имя</label>
          <input type="text" name="name" placeholder="Пожалуйста введите имя" required>
          <input type=submit>
        </form>
        '''
        return abort(Response(bad_response_text, status=400))

    try:
        resp = requests.get(f'{BACKEND_URL}/hello-by-name', params={'name': name})
    except Exception as e:
        bad_response_text = '''
        <!doctype html>
        <title>Ошибка! Не удалось сделать запрос до бэкенда!</title>
        <h1 style="color: red">Ошибка! Не удалось сделать запрос до бэкенда `{host}`! `{error}`.</h1>
        <form method=get>
          <label>Ваше имя</label>
          <input type="text" name="name" placeholder="Пожалуйста введите имя" required>
          <input type=submit>
        </form>
        '''.format(host=BACKEND_URL, error=e)
        return abort(Response(bad_response_text, status=400))

    if not resp.ok:
        bad_response_text = '''
        <!doctype html>
        <title>Ошибка! Бэкенд вернул ошибку!</title>
        <h1 style="color: red">Ошибка! Бэкенд вернул ошибку! `{}`.</h1>
        <form method=get>
          <label>Ваше имя</label>
          <input type="text" name="name" placeholder="Пожалуйста введите имя" required>
          <input type=submit>
        </form>
        '''.format(resp.content)
        return abort(Response(bad_response_text, status=400))

    data = resp.json()

    return '''
        <!doctype html>
        <title>{message}</title>
        <h1 style="color: green">{message}</h1>
        <form method=get>
          <label>Ваше имя</label>
          <input type="text" name="name" placeholder="Пожалуйста введите имя" value="{name}" required>
          <input type=submit>
        </form>
        
        '''.format(message=data.get('message', None), name=data.get('name', None))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
