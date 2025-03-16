from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db import get_session
from app.models.client import Client, ClientCreate
from app.models.motorcycle import Motorcycle

client_routes = APIRouter(prefix='/clients')

@client_routes.post('/create')
def create(
    client_data: ClientCreate,
    session: Session = Depends(get_session)
    ) -> Client:

    client = Client(
        name=client_data.name,
        email=client_data.email,
        phone=client_data.phone
    )
    session.add(client)

    if client_data.motorcycles:
        for bike in client_data.motorcycles:
            motorcycle_obj = Motorcycle(
                brand=bike.brand,
                model=bike.model,
                category=bike.category,
                cylinder_capacity=bike.cylinder_capacity,
                year_model=bike.year_model,
                service_manual=bike.service_manual,
                client=client
            )
            session.add(motorcycle_obj)

    session.commit()
    session.refresh(client)
    return client