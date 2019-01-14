import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.getenv('media_folder', 'media')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MAIL_SERVER = os.getenv('smtp_host', 'postfix')
MAIL_PORT = os.getenv('smtp_port', 25)
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = os.getenv('smtp_user', 'user')
MAIL_PASSWORD = os.getenv('smtp_password', 'password')
MAIL_DEFAULT_SENDER = 'user@gmail.com'

app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return 'Hello, World!'


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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/email/', methods=['get', 'post'])
def send_mail():
    if request.method == 'POST':
        mail_to = request.form.get('email')
        mail_head, mail_ms = request.form.get('title'), request.form.get('text', 'Hello')
        msg = Message(mail_head, sender='user@gmail.com', recipients=[mail_to])
        msg.body = mail_ms
        mail.send(msg)
        return '''
            <!doctype html>
            <title>Send email. SEND SUCCESS</title>
            <h1 style="color: green">SEND SUCCESS</h1>
            <form method=post>
              <input type="text" name="title" placeholder="title" required>
              <input type="email" name="email" placeholder="email to" required>
              <textarea name="text" placeholder="text message" required> </textarea>
              <input type=submit>
            </form>
            '''

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
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
