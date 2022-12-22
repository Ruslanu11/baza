from sql_base import base_worker
from sql_base import models


def new_position(position: models.Positions) -> int:
    base_worker.create_table("CREATE TABLE IF NOT EXISTS position(id INTEGER,salary INTEGER)")
    new_id = base_worker.execute("INSERT INTO position(id, salary) "
                                     "VALUES(?,?) "
                                     "RETURNING id", many = False,
                                     args=(position.id, position.salary,))
    return new_id

def get_position(position_id) -> int:
    query = f"SELECT salary FROM position WHERE id={position_id}"
    salary = base_worker.execute(query, many=False)
    return salary
    
def delete_position(position_id) -> int:
    query = f"DELETE FROM position WHERE id={position_id}"
    menu = base_worker.execute(query, many=False)
    return menu
