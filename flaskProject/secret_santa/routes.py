from flask import render_template, flash, redirect
from secret_santa import app
from secret_santa.forms import RegistrationForm
from dbhandler import reg_user


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Form submitted, name: {form.name.data}, address: {form.address.data}, email: {form.email.data}')
        reg_user(form.name.data, form.address.data, form.email.data)
        return redirect('/secretsanta')

    return render_template('Index.html', form=form)


@app.route('/secretsanta')
def secret_santa():
    return render_template('SecretSanta.html')
