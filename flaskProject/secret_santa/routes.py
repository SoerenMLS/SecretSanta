from flask import render_template
from secret_santa import app
from secret_santa.forms import RegistrationForm


@app.route('/')
@app.route('/index')
def index():
    form = RegistrationForm()
    return render_template('Index.html', title='Secret Santa', form=form)


@app.route('/submit')
def submit():
    return 'hello world'
