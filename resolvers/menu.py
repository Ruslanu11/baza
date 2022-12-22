from sql_base import base_worker
from sql_base import models


def new_menu(menu: models.Menu) -> int:
    base_worker.create_table("CREATE TABLE IF NOT EXISTS menu(id INTEGER,name TEXT, price INTEGER, unit_measurements INTEGER, weight INTEGER, ingradient TEXT)")
    new_id = base_worker.execute("INSERT INTO menu(id, name, price, unit_measurements, weight, ingradient) "
                                     "VALUES(?,?,?,?,?,?) "
                                     "RETURNING id", many=False,
                                     args=(menu.id, menu.name, menu.price, menu.unit_measurements, menu.weight, menu.ingradient))
    return new_id

def get_menu(menu_id) -> int:
    query = f"SELECT name, price, unit_measurements, weight, ingradient FROM menu WHERE id={menu_id}"
    menu = base_worker.execute(query, many=False)
    return menu

def delete_menu(menu_id) -> int:
    query = f"DELETE FROM menu WHERE id={menu_id}"
    menu = base_worker.execute(query, many=False)
    return menu

def update_menu(menu: models.Menu):
    new_id = base_worker.execute("UPDATE menu SET name = ?, price = ?, unit_measurements = ?, weight = ?, ingradient = ? WHERE id = ? RETURNING id", many=False,
                                     args=(menu.name, menu.price, menu.unit_measurements, menu.weight, menu.ingradient, menu.id))
    return new_id