from fastapi import APIRouter
from sql_base.models import Employees
import resolvers.employees

employee_router = APIRouter()


@employee_router.get('/')
def get_employees():
    return f'Response: {{text: Страница со списком рабочих }}'


@employee_router.post('/')
def new_employee(employee: Employees):
    new_id = resolvers.employees.new_employee(employee)
    return f'{{code: 201, id: {new_id}}}'


@employee_router.get('/{employee_id}')
def get_employee(employee_id: int):
    employee = resolvers.employees.get_employee(employee_id)
    return f'Employee: {employee}'


@employee_router.put('/{employee_id}')
def update_employee(employee: Employees):
    employee_id = resolvers.employees.update_employee(employee)
    return f'Update employee {employee_id}'


@employee_router.delete('/{employee_id}')
def delete_employee(employee_id: int):
    employee = resolvers.employees.delete_employee(employee_id)
    return f'delete employee {employee_id}'