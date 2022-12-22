from fastapi import APIRouter
from sql_base.models import Order
import resolvers.order

order_router = APIRouter()


@order_router.get('/')
def get_order():
    return f'Response: {{text: Страница со списком заказов }}'


@order_router.post('/')
def new_order(order: Order):
    new_id = resolvers.order.new_order(order)
    return f'{{code: 201, id: {new_id}}}'


@order_router.get('/{order_id}')
def get_order(order_id: int):
    order = resolvers.order.get_order(order_id)
    return f'order: {order}'


@order_router.put('/')
def update_order(order: Order):
    order_id = resolvers.order.update_order(order)
    return f'Update order {order_id}'


@order_router.delete('/{order_id}')
def delelte_order(order_id: int):
    order = resolvers.order.delete_order(order_id)
    return f'delete order {order_id}'