from fastapi import FastAPI
from sql_base import base_worker
from settings import BASE_PATH
from sql_base import models
from routers.orders import order_router
from routers.menu import menu_router
from routers.positions import position_router
from routers.employees import employee_router
from routers.stock import stock_router
from routers.unit_measurements import unit_measurements_router
from routers.users import user_router

base_worker.set_base_path(BASE_PATH)
 
if not base_worker.check_base():
    base_worker.create_base('../sql/base.sql')

app = FastAPI()
print("started")

@app.get("/")
def main_page():
    return {'page': 'Connection in correct'}


app.include_router(unit_measurements_router, prefix='/unit_measurements')
app.include_router(employee_router, prefix='/employees')
app.include_router(stock_router, prefix='/stock')
app.include_router(order_router, prefix='/order')
app.include_router(menu_router, prefix='/menu')
app.include_router(position_router, prefix='/position')
app.include_router(user_router, prefix='/users')



