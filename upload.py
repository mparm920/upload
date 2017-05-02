#!/usr/bin/python3
import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/opt/data'

app = Flask(__name__)
app.secret_key = 'eflex upload page'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No Selected File')
            return redirect(request.url)
        if file:
            print(file.filename)
            filename = secure_filename(file.filename) 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename))
    return render_template("main.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
