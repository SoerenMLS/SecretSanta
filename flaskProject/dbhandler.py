import sqlite3
import random
from pathlib import Path
from contextlib import closing

dbpath = str(Path(__file__).resolve().parent) + "/database/users.db"


def generate_id():
    return random.randint(1, 500000)


def reg_user(name, email, address):
    userid = generate_id()

    with closing(sqlite3.connect(dbpath)) as dbconnection:
        with dbconnection:
            with closing(dbconnection.cursor()) as cursor:
                cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (name, email, address, userid))

    print(f"added {name} to the db")
    return userid

