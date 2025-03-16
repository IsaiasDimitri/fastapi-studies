from typing import Any
from pydantic import field_validator
from sqlmodel import Relationship, SQLModel, Field

from app.models.motorcycle import Motorcycle, MotorcycleBase

class ClientBase(SQLModel):
    name: str
    phone: str
    email: str

class ClientCreate(ClientBase):
    motorcycles: list[MotorcycleBase] | None = None

class Client(ClientBase, table=True):
    id: int = Field(default=None, primary_key=True)
    motorcycles: list[Motorcycle] = Relationship(back_populates='client')