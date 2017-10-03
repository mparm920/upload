import os
from werkzeug.utils import secure_filename
from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required
from app import app

upload_blueprint = Blueprint(
    'upload', __name__,
    templates_folder='templates'
)

@upload_blueprint.route('/', methods=['GET', 'POST'])
@login_required
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
            return redirect(url_for('upload_file', filename=""))
    return render_template("main.html")