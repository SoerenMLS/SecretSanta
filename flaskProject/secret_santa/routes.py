from flask import render_template
from secret_santa import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('Index.html', title='Secret Santa')


@app.route('/submit')
def submit():
    return 'hello world'
