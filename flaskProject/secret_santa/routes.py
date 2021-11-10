import http.client
from santahandler import generate_session
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
        resp.set_cookie('userid', str(userid), max_age=604800)
        return resp

    return render_template('Index.html', form=form)


@app.route('/secretsanta', methods=['GET', 'POST'])
def secret_santa():
    user = get_user(request.cookies.get('userid'))
    form = JoinForm()
    if form.validate_on_submit():
        return "OMEGALUL"
    elif request.method == 'POST':
        print(request.json)

    return render_template('SecretSanta.html', form=form, name=user[0])


@app.route('/session/<session_id>')
def session(session_id):
    return session_id
    pass


@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        user_id = get_user(request.cookies.get('userid'))
        sessionid = generate_session(user_id)
        return redirect(f'/session/{sessionid}')

    return 'bad request', 400