from sql_base import base_worker
from sql_base import models


def new_stock(stock: models.Stock) -> int:
    base_worker.create_table("CREATE TABLE IF NOT EXISTS stock(id INTEGER, inradient TEXT, unit_measurement TEXT, weight INTEGER, unit_price INTEGER)")
    new_id = base_worker.execute("INSERT INTO stock(id, inradient, unit_measurement, weight, unit_price) "
                                     "VALUES(?, ?,?,?, ?) "
                                     "RETURNING id", many = False,
                                     args=(stock.id, stock.inradient, stock.unit_measurement, stock.weight, stock.unit_price))
    return new_id

def get_stock(stock_id) -> int:
    query = f"SELECT inradient, unit_measurement, weight, unit_price FROM stock WHERE id={stock_id}"
    stock = base_worker.execute(query, many=False)
    return stock
    
def delete_stock(stock_id) -> int:
    query = f"DELETE FROM stock WHERE id={stock_id}"
    menu = base_worker.execute(query, many=False)
    return menu

def update_stock(stock: models.Stock):
    new_id = base_worker.execute("UPDATE stock SET inradient= ?, unit_measurement = ?, weight = ?, unit_price = ? WHERE id = ? RETURNING id", many=False,
                                     args=(stock.inradient, stock.unit_measurement, stock.weight, stock.unit_price, stock.id))
    return new_id