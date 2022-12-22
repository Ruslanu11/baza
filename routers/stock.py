from fastapi import APIRouter
from sql_base.models import Stock
import resolvers.stock

stock_router = APIRouter()


@stock_router.get('/')
def get_stock():
    return f'Response: {{text: Страница со списком акций }}'

@stock_router.post('/')
def new_stock(stock: Stock):
    new_id = resolvers.stock.new_stock(stock)
    return f'{{code: 201, id: {new_id}}}'


@stock_router.get('/{stock_id}')
def get_stock(stock_id: int):
    stock = resolvers.stock.get_stock(stock_id)
    return f'stock: {{id: {stock}}}'


@stock_router.put('/')
def update_stock(stock: Stock):
    new_id = resolvers.stock.update_stock(stock)
    return f'Update stock {stock_id}'


@stock_router.delete('/{stock_id}')
def delelte_stock(stock_id: int):
    stock = resolvers.stock.delete_stock(stock_id)
    return f'delete stock {stock_id}'