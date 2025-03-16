from enum import Enum
from typing import Any
from pydantic import field_validator
from sqlmodel import SQLModel, Field, Relationship


class MotorcycleCategory(str, Enum):
    urban = 'urban'
    off_road = 'off_road'
    trail = 'trail'
    big_trail = 'big_trail'

class MotorcycleBase(SQLModel):
    brand: str
    model: str
    category: MotorcycleCategory | None = None
    cylinder_capacity: float | None = None
    year_model: str | None = None
    service_manual: str | None = None
    client_id: int | None = Field(foreign_key="client.id")

class MotorcycleCreate(MotorcycleBase):
    @field_validator('brand')
    @classmethod
    def ensure_brand_exists(cls, v: Any):
        if v not in ['honda', 'yamaha', 'shineray']:
            raise ValueError(f'{v} seems to not exists')
        return v

class Motorcycle(MotorcycleBase, table=True):
    plate: int = Field(default=None, primary_key=True)
    client: 'Client' = Relationship(back_populates='motorcycles')