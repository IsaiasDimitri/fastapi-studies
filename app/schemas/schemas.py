from pydantic import BaseModel
from enum import Enum
from datetime import date
from app.schemas.motorcycle import Motorcycle

class Seniority(str, Enum):
    junior = 'junior'
    chief = 'chief'

class OrderStatus(str, Enum):
    opened = 'opened'
    waiting_approval = 'waiting_approval'
    approved = 'approved'
    in_progress = 'in_progress'
    cancelled = 'cancelled'

class Client(BaseModel):
    name: str
    phone: str
    email: str
    motorcycles: list[Motorcycle] = []

class Mechanic(BaseModel):
    name: str
    phone: str
    email: str
    seniority: Seniority

class Service(BaseModel):
    name: str
    description: str
    minimun_seniority: Seniority | None = None

class Quote(BaseModel): # TODO improve that name
    services: list[Service] | None = None
    parts: dict[str, float] | None = None
    created_at: date
    updated_at: date

class ServiceOrder(BaseModel):
    mechanics: list[Mechanic]
    motorcycle: Motorcycle
    quote: Quote | None = None
    status: OrderStatus | None = None
    description: str
    created_at: date
    updated_at: date
    ready_at: date | None = None