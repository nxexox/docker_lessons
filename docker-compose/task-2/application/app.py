import os
import datetime

import requests
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

from flask_pymongo import PyMongo
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)


# Настройки приложения.
MINIO_HOST = '{}:{}'.format(os.getenv('MINIO_HOST'), os.getenv('MINIO_PORT'))
minio_client = Minio(MINIO_HOST,
                     access_key=os.getenv('MINIO_ACCESS_KEY'),
                     secret_key=os.getenv('MINIO_SECRET_KEY'),
                     secure=False)

MINIO_BUCKET_NAME = os.getenv('MINIO_BUCKET_NAME', 'backend_files')
# Создаем Bucket
try:
    minio_client.make_bucket(MINIO_BUCKET_NAME, location='us-east-1')
except BucketAlreadyOwnedByYou as err:
    pass
except BucketAlreadyExists as err:
    pass

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://{}:{}/{}'.format(
    os.getenv('MONGO_HOST'), os.getenv('MONGO_PORT'), os.getenv('MONGO_DATABASE')
)
mongo = PyMongo(app)

EMAIL_BACKEND_URI = 'http://{}:{}'.format(
    os.getenv('EMAIL_SERVICE_HOST', 'postfix_backend'),
    os.getenv('EMAIL_SERVICE_PORT', 5000)
)


# Хэндлеры
@app.route('/upload-file/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file_bytes = file.read()
            file.seek(0)
            minio_client.put_object(
                MINIO_BUCKET_NAME, filename, file, len(file_bytes)
            )
            mongo.db.uploads.insert(
                {'bucket': MINIO_BUCKET_NAME, 'filename': filename,
                 'size': len(file_bytes), 'date_upload': datetime.datetime.now().isoformat()}
            )
            # return redirect('/upload-file/')

    docs = list(mongo.db.uploads.find({}))
    documents = '<ul>{}</ul>'.format(
        ''.join([
            '<li>Bucket: `{}`, Filename: `{}`, Filesize: `{}`, Date Upload: `{}`</li>'.format(
                doc.get('bucket', ''), doc.get('filename', ''),
                doc.get('size', ''), doc.get('date_upload', '')
            )
            for doc in docs
        ])
    )

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <h2>Uploaded files(Mongo DATA): {}<h2>
    {}
    '''.format(len(docs), documents)


@app.route('/email/', methods=['get', 'post'])
def send_mail():
    if request.method == 'POST':
        mail_to = request.form.get('email')
        mail_head, mail_ms = request.form.get('title'), request.form.get('text', 'Hello')
        resp = requests.post(EMAIL_BACKEND_URI, json={
            'email': mail_to, 'title': mail_head, 'text': mail_ms
        })
        mongo.db.emails.insert({
            'status': resp.status_code, 'date': datetime.datetime.now().isoformat(),
            **resp.json()
        })

    emails = list(mongo.db.emails.find({}))
    emails_str = '<ul>{}</ul>'.format(
        ''.join([
            '<li>Status: `{}`, Date: `{}`, Other Information: `{}`</li>'.format(
                doc.pop('status', ''), doc.pop('date', ''), doc
            )
            for doc in emails
        ])
    )

    return '''
    <!doctype html>
    <title>Send email</title>
    <h1>Send email</h1>
    <form method=post>
      <input type="text" name="title" placeholder="title" required>
      <input type="email" name="email" placeholder="email to" required>
      <textarea name="text" placeholder="text message" required> </textarea>
      <input type=submit>
    </form>
    <h2>Send mails(Данные из Монги): {}</h2>
    {}
    '''.format(len(emails), emails_str)


@app.route('/')
def hello_world():
    return """
    <!doctype html>
    <title>Главная страница</title>
    <h1>Оглавление:</h1>
    <ul>
    <li><a href="/upload-file/">Загрузить файл в s3 storage</a></li>
    <li><a href="/email/">Отправить письмо на почту</a></li>
    </ul>
    """


# Запускаем приложение
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('BACKEND_PORT', 5000))
