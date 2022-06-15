import time, os, pyqrcode, png, csv, sys
from flask import Flask, render_template, redirect, url_for, request, send_file
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import reportqr

app = Flask(__name__,static_folder='static')

app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

cur_path = os.path.dirname(__file__)

Bootstrap(app)

name_name = ""

class NameForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    asset_tag = StringField('Asset Tag', validators=[DataRequired()])
    advisor = StringField('Advisor', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    message = ""
    global name_name
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        asset_tag = form.asset_tag.data
        advisor = form.advisor.data
        file = asset_tag + ".pdf"
        reportqr.make_pdf(name,email,asset_tag,advisor)
        name_name = name
        return redirect('/human/'+file)
    return render_template('index.html', form=form, message=message)

@app.route('/human/<file>', methods = ['GET'])
def human(file):
    name = name_name
    return render_template('human.html', name=name, file=file)

@app.route('/moreinfo')
def moreinfo():
    return render_template('moreinfo.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# keep this as is
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
