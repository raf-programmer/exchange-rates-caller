from datetime import datetime
from typing import Optional

from pydantic import BaseModel, constr


class Call(BaseModel):
    from_currency: constr(min_length=2, max_length=8)
    to_currency: constr(min_length=2, max_length=8)
    amount: int
    when: Optional[datetime]


class DisplayCall(Call):
    id: int
    converted_value: float

    class Config:
        orm_mode = True
