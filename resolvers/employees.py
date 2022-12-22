from sql_base import base_worker
from sql_base import models


def new_employee(employee: models.Employees ) -> int:
    base_worker.create_table("CREATE TABLE IF NOT EXISTS employee(id INTEGER, telephone TEXT, job_title TEXT)")
    new_id = base_worker.execute("INSERT INTO employee(id, telephone, job_title) "
                                     "VALUES(?,?,?) "
                                     "RETURNING id",many=False,
                                     args=(employee.id, employee.telephone, employee.job_title))
    return new_id
    
def get_employee(employee_id) -> int:
    query = f"SELECT telephone, job_title FROM employee WHERE id={employee_id}"
    employee = base_worker.execute(query, many=False)
    return employee

def delete_employee(employee_id) -> int:
    query = f"DELETE FROM employee WHERE id={employee_id}"
    menu = base_worker.execute(query, many=False)
    return menu

def update_employee(employee: models.Employees):
    new_id = base_worker.execute("UPDATE employee SET telephone = ?, job_title = ? WHERE id = ? RETURNING id", many=False,
                                     args=(employee.telephone, employee.job_title, employee.id))
    return new_id