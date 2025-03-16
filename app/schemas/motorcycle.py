from enum import Enum
from typing import Any
from pydantic import BaseModel, field_validator

class MotorcycleCategory(str, Enum):
    urban = 'urban'
    off_road = 'off_road'
    trail = 'trail'
    big_trail = 'big_trail'

class MotorcycleBase(BaseModel):
    brand: str
    model: str
    category: MotorcycleCategory
    cylinder_capacity: float
    year_model: str
    service_manual: str

class MotorcycleCreate(MotorcycleBase):
    @field_validator('brand')
    @classmethod
    def ensure_foobar(cls, v: Any):
        if 'foobar' not in v:
            raise ValueError('"foobar" not found in a')
        return v

class MotorcycleWithID(MotorcycleBase):
    plate: int