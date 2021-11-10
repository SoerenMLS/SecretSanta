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
    print(user)
    return user


def reg_session(session_id):
    with closing(sqlite3.connect(dbpath)) as dbconnection:
        with dbconnection:
            with closing(dbconnection.cursor()) as cursor:
                cursor.execute("INSERT INTO session VALUES (?)", (session_id,))


def add_user_to_session(user_id, session_id):
    with closing(sqlite3.connect(dbpath)) as dbconnection:
        with dbconnection:
            with closing(dbconnection.cursor()) as cursor:
                cursor.execute("INSERT INTO user_sessions VALUES (?, ?)", (user_id, session_id))
