import sqlite3
import random
from pathlib import Path
from contextlib import closing

dbpath = str(Path(__file__).resolve().parent) + "/database/users.db"


def generate_id():
    return random.randint(1, 2000000)


def reg_user(name, email, address):
    userid = generate_id()

    with closing(sqlite3.connect(dbpath)) as dbconnection:
        with dbconnection:
            with closing(dbconnection.cursor()) as cursor:
                cursor.execute("INSERT INTO users (name, address, email, id) VALUES (?, ?, ?, ?)", (name, email, address, userid))

    print(f"added {name} to the db")
    return userid


def get_user(user_id):
    with closing(sqlite3.connect(dbpath)) as dbconnection:
        with dbconnection:
            with closing(dbconnection.cursor()) as cursor:
                user = cursor.execute("SELECT * FROM users WHERE id = (?)", (user_id,)).fetchone()
    return user


def reg_session(session_id, owner_id, invitation):
    with closing(sqlite3.connect(dbpath)) as dbconnection:
        with dbconnection:
            with closing(dbconnection.cursor()) as cursor:
                cursor.execute("INSERT INTO session VALUES (?,?,?)", (session_id, owner_id, invitation))


def add_user_to_session(user_id, session_id):
    with closing(sqlite3.connect(dbpath)) as dbconnection:
        with dbconnection:
            with closing(dbconnection.cursor()) as cursor:
                cursor.execute("INSERT INTO user_sessions VALUES (?, ?)", (user_id, session_id))


def session_exists(session_id):
    with closing(sqlite3.connect(dbpath)) as dbconnection:
        with dbconnection:
            with closing(dbconnection.cursor()) as cursor:
                val = cursor.execute("SELECT EXISTS(SELECT 1 FROM session WHERE session_id = (?))", (session_id,)).fetchone()

    if val[0] == 1:
        return True
    else:
        return False


def user_is_invited(invitation, invite_mail):
    with closing(sqlite3.connect(dbpath)) as dbconnection:
        with dbconnection:
            with closing(dbconnection.cursor()) as cursor:
                val = cursor.execute("SELECT EXISTS(SELECT 1 FROM session WHERE invite_code = (?))", (invitation,)).fetchone()

                if val[0] == 1:
                    invited_mails = cursor.execute("SELECT invited_email FROM session_invites WHERE session_invite = (?)", (invitation,)).fetchone()
                    if invite_mail in invited_mails:
                        return True

    return False


def get_session_from_invite(invite_code):
    with closing(sqlite3.connect(dbpath)) as dbconnection:
        with dbconnection:
            with closing(dbconnection.cursor()) as cursor:
                val = cursor.execute("SELECT session_id FROM session WHERE invite_code = (?)", (invite_code,)).fetchone()
    return val


def get_session_from_id(session_id):
    with closing(sqlite3.connect(dbpath)) as dbconnection:
        with dbconnection:
            with closing(dbconnection.cursor()) as cursor:
                val = cursor.execute("SELECT * FROM session WHERE session_id = (?)", (session_id,)).fetchone()
    return val
