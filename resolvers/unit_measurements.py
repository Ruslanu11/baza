from sql_base import base_worker
from sql_base import models


def new_unit_measurements(unit_measurement: models.Unit_measurements) -> int:
    base_worker.create_table("CREATE TABLE IF NOT EXISTS unit_measurements(id INTEGER,unit_measurement TEXT)")
    new_id = base_worker.execute("INSERT INTO unit_measurements(id, unit_measurement) "
                                     "VALUES(?,?) "
                                     "RETURNING id", many=False,
                                     args=(unit_measurement.id, unit_measurement.unit_measurement,))
    return new_id

def get_unit_measurement(unit_measurement_id) -> int:
    query = f"SELECT unit_measurement FROM unit_measurements WHERE id={unit_measurement_id}"
    unit_measurement = base_worker.execute(query, many=False)
    return unit_measurement

def delete_unit_measurement(unit_measurement_id) -> int:
    query = f"DELETE FROM unit_measurements WHERE id={unit_measurement_id}"
    menu = base_worker.execute(query, many=False)
    return menu

def update_unit_measurement(unit_measurement: models.Unit_measurements):
    new_id = base_worker.execute("UPDATE unit_measurements SET unit_measurement = ? WHERE id = ? RETURNING id", many=False,
                                     args=(unit_measurement.unit_measurement,unit_measurement.id))
    return new_id