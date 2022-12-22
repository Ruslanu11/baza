from fastapi import APIRouter
from sql_base.models import User
from resolvers import users

user_router = APIRouter()


@user_router.get('/')
def not_login():
    return {"Message": "Login in system"}


@user_router.post('/login')
def check_login(user: User, ):
    post = users.check_login(user)
    if post:
        return {"code": 200, "message": "Login correct", 'post': post}
    else:
        return {"code": 401, "message": "Login incorrect, try again", 'post': None}
