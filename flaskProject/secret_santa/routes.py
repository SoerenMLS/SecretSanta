from flask import render_template, flash, redirect, request, make_response
from secret_santa import app
from secret_santa.forms import RegistrationForm, JoinForm
from dbhandler import reg_user, get_user


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    cookie = request.cookies.get("userid")
    print(cookie)

    if cookie is not None:
        return redirect('/secretsanta')

    if form.validate_on_submit():
        userid = reg_user(form.name.data, form.address.data, form.email.data)
        flash(f'{form.name.data}, You have been registered! your user-id is: {userid}, write it down!')
        resp = make_response(redirect('/secretsanta'))
        resp.set_cookie('userid', str(userid))
        return resp

    return render_template('Index.html', form=form)


@app.route('/secretsanta', methods=['GET', 'POST'])
def secret_santa():
    user = get_user(request.cookies.get('userid'))
    form = JoinForm()
    if form.validate_on_submit():
        return "OMEGALUL"
    elif request.method == 'POST':
        pass

    return render_template('SecretSanta.html', form=form, name=user[0])
