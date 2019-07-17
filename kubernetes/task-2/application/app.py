from flask import Flask, request, abort, Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''
        <!doctype html>
        <title>Главная страница</title>
        <h1>Что умеет ваше приложение:</h1>
        <ul>
        <li><a href="/hello-by-name?name=Неизвестный">Приветствие по имени</a></li>
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

    return '''
        <!doctype html>
        <title>Привет {name}!</title>
        <h1 style="color: green">Привет {name}!</h1>
        <form method=get>
          <label>Ваше имя</label>
          <input type="text" name="name" placeholder="Пожалуйста введите имя" value="{name}" required>
          <input type=submit>
        </form>
        '''.format(name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
