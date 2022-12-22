
from typing import Optional
from pydantic import BaseModel

#1
class Unit_measurements(BaseModel):
    id:Optional [int]
    unit_measurement: str
#2
class Stock(BaseModel):
    id: Optional [int]
    inradient: str
    unit_measurement: int
    weight: int
    unit_price: int
#3
class Menu(BaseModel):
    id: Optional [int]
    name: str
    price: int
    unit_measurements: int
    weight: int
    ingradient: str
#4
class Order(BaseModel):
    id: Optional [int]
    dish: str
    salesman: str
    cook: str
#5
class Employees(BaseModel):
    id: Optional [int]
    telephone: int
    job_title: str
#6
class Positions(BaseModel):
    id: Optional [int]
    salary: int

#6
class User(BaseModel):
    id: Optional [int]
    login: str
    password: str