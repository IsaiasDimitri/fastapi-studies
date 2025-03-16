from typing import Annotated
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from app.db import get_session
from app.models.motorcycle import MotorcycleCategory, MotorcycleCreate, Motorcycle

# motorcycle_list = [
#     { 'plate': 0, 'brand': 'honda', 'model': 'pop', 'category': MotorcycleCategory.urban, \
#         'cylinder_capacity': 109.3, 'year_model': '2023/2024', 'service_manual': 'somelink'},
#     { 'plate': 1, 'brand': 'yamaha', 'model': 'crosser', 'category': MotorcycleCategory.trail, \
#         'cylinder_capacity': 150.0, 'year_model': '2021/2021', 'service_manual': 'somelink'},
#     { 'plate': 2,'brand': 'shineray', 'model': 'Phoenix S', 'category': MotorcycleCategory.off_road, \
#         'cylinder_capacity': 50.0, 'year_model': '2024/2024', 'service_manual': 'somelink'}
# ]

motorcycle_routes = APIRouter(prefix='/motorcycles')

# @motorcycle_routes.get('/')
# def get_all_motorcycles(
#     type: MotorcycleCategory | None = None,
#     contains: Annotated[str | None, Query(max_length=10)] = None
#     ) -> list[Motorcycle]:
#     motorcycles = [
#         Motorcycle(**bike) for bike in motorcycle_list
#     ]
#     if type:
#         motorcycles = [
#             bike for bike in motorcycles if bike.category.lower() == type.lower()
#         ]
#     if contains:
#         motorcycles = [
#             bike for bike in motorcycles if contains.lower() \
#                                             in bike.brand.lower() \
#                                             or contains.lower() in bike.model.lower()
#         ]
#     return motorcycles

@motorcycle_routes.post('/create')
def create_motorcycle(
    motorcycle_data: MotorcycleCreate,
    session: Session = Depends(get_session)
    ) -> Motorcycle:

    motorcycle = Motorcycle(
        brand=motorcycle_data.brand,
        model=motorcycle_data.model,
        category=motorcycle_data.category,
        cylinder_capacity=motorcycle_data.cylinder_capacity,
        year_model=motorcycle_data.year_model,
        service_manual=motorcycle_data.service_manual
    )
    session.add(motorcycle)
    session.commit()
    session.refresh(motorcycle)
    
    return motorcycle
