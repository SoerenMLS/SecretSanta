from santahandler import generate_session, join_session, get_session
from flask import render_template, flash, redirect, request, make_response
from secret_santa import app
from secret_santa.forms import RegistrationForm, JoinForm
from dbhandler import reg_user, get_user, session_exists
from secret_santa.tables import table


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
        joined_session = join_session(user, form.invitation.data)
        if joined_session:
            return redirect(f'/session/{joined_session}')
        else:
            flash(f"I'm sorry but you're not invited to this session")
    elif request.method == 'POST':
        print(request.json)

    return render_template('SecretSanta.html', form=form, name=user[0])


@app.route('/session/<session_id>')
def session(session_id):
    if session_exists(session_id):
        user = get_user(request.cookies.get('userid'))
        print(user)
        current_session = get_session(session_id)
        flash(f"session invitation is: {current_session.invitation}")
        return render_template('session.html', table=table, session_name=session_id)

    flash(f"session: '{session_id}' does not exist")
    return redirect('/secretsanta')


@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        request_json = request.json
        generated_session = generate_session(request_json['userid'])
        return redirect(f'/session/{generated_session.session_id}')

    return 'bad request', 400

