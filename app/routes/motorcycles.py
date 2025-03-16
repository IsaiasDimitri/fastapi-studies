from typing import Annotated
from fastapi import APIRouter, Query
from app.schemas.motorcycle import MotorcycleCategory, MotorcycleCreate, MotorcycleWithID

motorcycle_list = [
    { 'plate': 0, 'brand': 'honda', 'model': 'pop', 'category': MotorcycleCategory.urban, \
        'cylinder_capacity': 109.3, 'year_model': '2023/2024', 'service_manual': 'somelink'},
    { 'plate': 1, 'brand': 'yamaha', 'model': 'crosser', 'category': MotorcycleCategory.trail, \
        'cylinder_capacity': 150.0, 'year_model': '2021/2021', 'service_manual': 'somelink'},
    { 'plate': 2,'brand': 'shineray', 'model': 'Phoenix S', 'category': MotorcycleCategory.off_road, \
        'cylinder_capacity': 50.0, 'year_model': '2024/2024', 'service_manual': 'somelink'}
]

motorcycle_routes = APIRouter(prefix='/motorcycles')

@motorcycle_routes.get('/')
def get_all_motorcycles(
    type: MotorcycleCategory | None = None,
    contains: Annotated[str | None, Query(max_length=10)] = None
    ) -> list[MotorcycleWithID]:
    motorcycles = [
        MotorcycleWithID(**bike) for bike in motorcycle_list
    ]
    if type:
        motorcycles = [
            bike for bike in motorcycles if bike.category.lower() == type.lower()
        ]
    if contains:
        motorcycles = [
            bike for bike in motorcycles if contains.lower() \
                                            in bike.brand.lower() \
                                            or contains.lower() in bike.model.lower()
        ]
    return motorcycles

@motorcycle_routes.post('/create')
def create_motorcycle(motorcycle: MotorcycleCreate) -> MotorcycleWithID:
    plate = motorcycle_list[-1]['plate'] + 1
    bike = MotorcycleWithID(plate=plate, **motorcycle.model_dump())
    motorcycle_list.append(motorcycle.model_dump())
    return bike
