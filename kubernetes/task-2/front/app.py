import os
import socket

from flask import Flask, request, abort, Response
import requests

app = Flask(__name__)

RAISE_IF_NOT_VALID_BACKEND_URL = os.getenv('RAISE_IF_NOT_VALID_BACKEND_URL', 'false')
BACKEND_URL = os.getenv('BACKEND_URL', 'http://0.0.0.0:5001')
if RAISE_IF_NOT_VALID_BACKEND_URL.lower() != 'false' and not BACKEND_URL:
    raise ValueError('Environ `BACKEND_URL` not found in system. Please check environment settings.')

name = os.getenv('USER_NAME', 'Неизвестный')
host = socket.gethostname()


def calculate_html_render(a=None, b=None, operation=None, result=None, history=None, error=None):
    return '''
        <!doctype html>
        <title>Калькулятор</title>
        <a href="/"><-- Назад</a>
        {error}
        <h1>Привет "{front_name}", ты на сервере: {front_host}</h1>
        <h2>Калькулятор вычисляет выражение a (+ - * /) b = </h2>
        <form method=post>
          <label>a=</label>
          <input type="number" name="a" value="{a}" placeholder="а=" required>
          <label>Операция=</label>
          <select name="operation" required>
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
          </select>
          <label>b=</label>
          <input type="number" name="b" value="{b}" placeholder="b=" required>
          <label>==</label>
          <input type="number" name="result" value="{result}" placeholder="Тут будет результат" required disabled>
          <input type=submit>
        </form>
        <h2>История расчетов {backend_server}: </h2>
        <ul>{history}</ul>
    '''.format(
        front_name=name, front_host=host,
        error=f'<h1 style="color: red">{error}</h1>' if error else '',
        a=a if a else '', b=b if b else '',
        result=result if result else '',
        history=''.join(map(
            lambda x: f'<li><b>{x["datetime"]}</b>: {x["a"]} {x["operation"]} {x["b"]} = {x["result"]}</li>',
            history
        )) if history else '',
        backend_server='(Взята с бэкенд сервера {})'.format(history[0]['host']) if history else ''
    )


@app.route('/', methods=['GET'])
def index():
    return '''
        <!doctype html>
        <title>Главная страница</title>
        <h1>Привет "{front_name}", ты на сервере: {front_host}</h1>
        <h2>Что умеет ваше приложение:</h2>
        <ul>
        <li><a href="/hello-by-name?name=Неизвестный">Приветствие по имени</a></li>
        <li><a href="/calculate">Калькулятор</a></li>
        </ul>
        '''.format(front_name=name, front_host=host)


@app.route('/hello-by-name', methods=['GET'])
def hello_by_name():
    try:
        resp = requests.get(f'{BACKEND_URL}/hello-by-name')
    except Exception as e:
        bad_response_text = '''
        <!doctype html>
        <title>Ошибка! Не удалось сделать запрос до бэкенда!</title>
        <h1>Привет "{front_name}", ты на сервере: {front_host}</h1>
        <a href="/"><-- Назад</a>
        <h2 style="color: red">Ошибка! Не удалось сделать запрос до бэкенда `{host}`! `{error}`.</h2>
        '''.format(host=BACKEND_URL, error=e, front_name=name, front_host=host)
        return abort(Response(bad_response_text, status=400))

    if not resp.ok:
        bad_response_text = '''
        <!doctype html>
        <title>Ошибка! Бэкенд вернул ошибку!</title>
        <h1>Привет "{front_name}", ты на сервере: {front_host}</h1>
        <a href="/"><-- Назад</a>
        <h2 style="color: red">Ошибка! Бэкенд вернул ошибку! `{content}`.</h2>
        '''.format(content=resp.content, front_name=name, front_host=host)
        return abort(Response(bad_response_text, status=400))

    data = resp.json()

    return '''
        <!doctype html>
        <title>{message}</title>
        <a href="/"><-- Назад</a>
        <h1>Привет "{front_name}", ты на сервере: {front_host}</h1>
        <h2>Бэкенд сервер: {back_host}</h2>
        <h2 style="color: green">{message}</h2>
        <h2>История запросов:<h2>
        <ul>
            {history}
        </ul>
        
        '''.format(
        front_name=name, front_host=host,
        back_name=data.get('name', None), back_host=data.get('host', None),
        message=data.get('message', None),
        history=''.join(map(lambda x: f'<li>{x}</li>', data.get('history_names', [])))
    )


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'GET':
        try:
            resp = requests.get(f'{BACKEND_URL}/calculate/history')
            history = resp.json().get('history', [])
            return calculate_html_render(history=history)
        except Exception:
            pass
        return calculate_html_render()
    else:
        a, b = request.form.get('a', None), request.form.get('b', None)
        operation = request.form.get('operation', None)

        try:
            resp = requests.post(f'{BACKEND_URL}/calculate', json={
                'a': a, 'b': b, 'operation': operation
            })
        except Exception as e:
            return abort(Response(calculate_html_render(
                error=e
            ), status=400))

        result, history, error = resp.json().get('result', None), [], None
        try:
            resp_history = requests.get(f'{BACKEND_URL}/calculate/history')
            history = resp_history.json().get('history', [])
        except Exception as e:
            error = f'Не удалось загрузить историю `{e}`'

        return calculate_html_render(a=a, b=b, operation=operation, history=history, error=error, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
