import os

from flask import Flask, request, abort, Response
import requests

app = Flask(__name__)


BACKEND_URL = os.getenv('BACKEND_URL', 'http://0.0.0.0:5001')
if not BACKEND_URL:
    raise ValueError('Environ `BACKEND_URL` not found in system. Please check environment settings.')


def calculate_html_render(a=None, b=None, operation=None, result=None, history=None, error=None):
    return '''
        <!doctype html>
        <title>Калькулятор</title>
        <a href="/"><-- Назад</a>
        {error}
        <h1>Калькулятор, введите данные для расчета</h1>
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
        <h2>История расчетов: </h2>
        <ul>{history}</ul>
    '''.format(
        error=f'<h1 style="color: red">{error}</h1>' if error else '',
        a=a if a else '', b=b if b else '',
        result=result if result else '',
        history=''.join(map(
            lambda x: f'<li>{x["a"]} {x["operation"]} {x["b"]} = {x["result"]}</li>',
            history
        )) if history else ''
    )


@app.route('/', methods=['GET'])
def index():
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


@app.route('/jobs/list', methods=['GET'])
def job_list():
    try:
        resp = requests.get(f'{BACKEND_URL}/jobs/list')
    except Exception as e:
        bad_response_text = '''
            <!doctype html>
            <a href="/"><-- Назад</a>
            <title>Не удалось загрузить страницу</title>
            <h1 style="color: red">Не удалось загрузить страницу со список jobs. `{error}`</h1>
        '''.format(error=e)
        return abort(Response(bad_response_text, status=400))

    jobs = resp.json().get('items', [])
    return '''
        <!doctype html>
        <title>Список выполненных JOBS</title>
        <a href="/"><-- Назад</a>
        <h1 style="color: green">Список выполненных JOBS. Всего: {count}</h1>
        <ul>
            {jobs}
        </ul>
    '''.format(
        count=len(jobs),
        jobs=''.join(map(
            lambda x: f'<li>Date: {x["date"]}, Message: {x["message"]}</li>',
            jobs
        ))
    )


@app.route('/hello-by-name', methods=['GET'])
def hello_by_name():
    name = request.args.get('name', None)
    if not name:
        bad_response_text = '''
        <!doctype html>
        <title>Ошибка! Пожалуйста введите имя!</title>
        <a href="/"><-- Назад</a>
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
        <a href="/"><-- Назад</a>
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
        <a href="/"><-- Назад</a>
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
        <a href="/"><-- Назад</a>
        <h1 style="color: green">{message}</h1>
        <form method=get>
          <label>Ваше имя</label>
          <input type="text" name="name" placeholder="Пожалуйста введите имя" value="{name}" required>
          <input type=submit>
        </form>
        
        <h2>История запросов:<h2>
        <ul>
            {history}
        </ul>
        
        '''.format(
        message=data.get('message', None),
        name=data.get('name', None),
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
