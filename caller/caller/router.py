from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from caller import db

from . import schema, services

router = APIRouter(tags=["CallModel"], prefix="/caller")


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schema.DisplayCall
)
async def call_for_convert_currencies(
    call: schema.Call, database: Session = Depends(db.get_db)
):
    new_call = await services.call_for_convert_currencies(call, database)
    return new_call


@router.get("/", response_model=List[schema.DisplayCall])
async def get_all_calls(database: Session = Depends(db.get_db)):
    return await services.get_all_calls(database)
