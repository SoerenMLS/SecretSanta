from essential_generators import DocumentGenerator

from dbhandler import reg_session, add_user_to_session, get_session_from_invite, user_is_invited, get_session_from_id
gen = DocumentGenerator()


class Session:
    def __init__(self, session_id, owner_id, invitation):
        self.owner_id = owner_id
        self.invitation = invitation
        self.session_id = session_id


def generate_session(owner_id):
    session_id = gen.slug()
    invite = gen.word() + gen.word()
    reg_session(session_id, owner_id, invite)

    add_user_to_session(owner_id, session_id)

    return Session(session_id, owner_id, invite)


def join_session(user, invite_id):
    if user_is_invited(invite_id, user[2]):
        active_session = get_session_from_invite(invite_id)
        add_user_to_session(user[3], active_session[0])
        return active_session
    else:
        return False


def get_session(session_id):
    ses = get_session_from_id(session_id)
    return Session(ses[0], ses[1], ses[2])


def get_participants(session_id):
    pass
