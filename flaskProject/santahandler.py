from essential_generators import DocumentGenerator
from dbhandler import reg_session, add_user_to_session

gen = DocumentGenerator()


def generate_session(user_id):
    session_id = gen.slug()
    reg_session(session_id)
    add_user_to_session(user_id, session_id)
    return session_id
