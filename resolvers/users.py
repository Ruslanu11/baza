from sql_base import models
from sql_base import base_worker


def check_login(user: models.User) -> int:
    query = "SELECT post FROM users WHERE login = ? AND password = ?"
    post_id = base_worker.execute(query,  many=False, args = (user.login, user.password))
    return post_id