from utils.db_api.Database import Users as Users_


def Users():
    return [i for i in Users_.select()]


def Statistica():
    users = Users_.select().count()
    return [users]


def User(chat_id):
    try:
        Users_.create(chat_id=chat_id)
    except:
        pass
