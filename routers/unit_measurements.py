from fastapi import APIRouter
from sql_base.models import Unit_measurements
import resolvers.unit_measurements

unit_measurements_router = APIRouter()


@unit_measurements_router.get('/')
def get_unit_measurements():
    return f'Response: {{text: Страница со списком измерений }}'


@unit_measurements_router.post('/')
def new_unit_measurements(unit_measurements: Unit_measurements):
    new_id = resolvers.unit_measurements.new_unit_measurements(unit_measurements)
    return f'{{code: 201, id: {new_id}}}'


@unit_measurements_router.get('/{measure_id}')
def get_unit_measurements(measure_id: int):
    unit_measurements = resolvers.unit_measurements.get_unit_measurements(measure_id)
    return f'unit_measurements: id: {unit_measurements}'


@unit_measurements_router.put('/')
def update_unit_measurements(unit_measurements: Unit_measurements):
    measure_id = resolvers.unit_measurements.update_unit_measurements(unit_measurements)
    return f'Update unit_measurements {measure_id}'


@unit_measurements_router.delete('/{measure_id}')
def delelte_unit_measurements(measure_id: int):
    unit_measurements = resolvers.unit_measurements.delete_unit_measurements(measure_id)
    return f'delete unit_measurements {measure_id}'