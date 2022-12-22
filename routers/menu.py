from fastapi import APIRouter
from sql_base.models import Menu
import resolvers.menu

menu_router = APIRouter()


@menu_router.get('/')
def get_menu():
    return f'Response: {{text: Страница со списком меню }}'


@menu_router.post('/')
def new_menu(menu: Menu):
    new_id = resolvers.menu.new_menu(menu)
    return f'{{code: 201, id: {new_id}}}'


@menu_router.get('/{menu_id}')
def get_menu(menu_id: int):
    menu = resolvers.menu.get_menu(menu_id)
    return f'menu: {{id: {menu}}}'


@menu_router.put('/')
def update_menu(menu: Menu):
    menu_id = resolvers.menu.update_menu(menu)
    return f'Update menu {menu_id}'


@menu_router.delete('/{menu_id}')
def delete_menu(menu_id: int):
    menu = resolvers.menu.delete_menu(menu_id)
    return f'delete menu {menu_id}'