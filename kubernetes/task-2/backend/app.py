import os
import socket
import operator
from datetime import datetime

from flask import Flask, request, jsonify, abort, make_response

app = Flask(__name__)

name = os.getenv('USER_NAME', 'бэкенд')
host = socket.gethostname()


JOB_MESSAGES = []
VALID_OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
HELLO_BY_NAME_NAMES = []
CALCULATION_HISTORY = []


@app.route('/hello-by-name', methods=['GET'])
def hello_by_name():
    HELLO_BY_NAME_NAMES.append((name, host))
    return jsonify({
        'message': f'Привет {name}', 'name': name,
        'host': host,
        'history_names': list(reversed(HELLO_BY_NAME_NAMES))
    })


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json(force=True)
    a, b, operation = data.get('a', None), data.get('b', None), data.get('operation', None)
    try:
        a, b = int(a), int(b)
    except Exception:
        abort(make_response(jsonify(message='`a`, `b` must be integers.'), 400))

    operation_func = VALID_OPERATIONS.get(operation, None)
    if not operation_func:
        abort(make_response(jsonify(message=f'Invalid operation `{operation}`'), 400))

    try:
        result = operation_func(a, b)
    except Exception as e:
        result = str(e)

    result_data = dict(
        a=a, b=b, operation=operation,
        result=result,
        name=name, host=host, datetime=datetime.now()
    )
    CALCULATION_HISTORY.append(result_data)

    return jsonify(result_data)


@app.route('/calculate/history', methods=['GET'])
def calculate_history():
    return jsonify(history=list(reversed(CALCULATION_HISTORY)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
