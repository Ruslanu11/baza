from fastapi import APIRouter
from sql_base.models import Positions
import resolvers.positions

position_router = APIRouter()


@position_router.get('/')
def get_positions():
    return f'Response: {{text: Страница со списком позиций }}'


@position_router.post('/')
def new_position(position: Positions):
    new_id = resolvers.positions.new_position(position)
    return f'{{code: 201, id: {new_id}}}'


@position_router.get('/{position_id}')
def get_position(position_id: int):
    position = resolvers.positions.get_position(position_id)
    return f'positions: {{id: {position}}}'


@position_router.put('/')
def update_position(position: Positions):
    position_id = resolvers.positions.update_position(position)
    return f'Update position {position_id}'


@position_router.delete('/{position_id}')
def delelte_position(position_id: int):
    position = resolvers.positions.delete_position(position_id)
    return f'delete position {position_id}'