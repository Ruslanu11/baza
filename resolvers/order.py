from sql_base import base_worker
from sql_base import models


def new_order(order: models.Order) -> int:
    base_worker.create_table("CREATE TABLE IF NOT EXISTS orders(id INTEGER, dish TEXT, salesman TEXT, cook TEXT)")
    new_id = base_worker.execute("INSERT INTO orders(id, dish, salesman, cook) "
                                     "VALUES(?,?,?,?)"
                                     "RETURNING id", many = False,
                                     args=(order.id, order.dish, order.salesman, order.cook))
    return new_id

def get_order(order_id) -> int:
    query = f"SELECT * FROM orders WHERE id={order_id}"
    print(query)
    order = base_worker.execute(query, many=False)
    return order

def delete_order(order_id) -> int:
    query = f"DELETE FROM orders WHERE id={order_id}"
    print(query)
    order = base_worker.execute(query, many=False)
    return order

def update_order(order: models.Order):
    new_id = base_worker.execute("UPDATE orders SET dish = ?, salesman = ?, cook = ? WHERE id = ? RETURNING id", many=False,
                                     args=(order.dish, order.salesman, order.cook, order.id))
    return new_id