from typing import List

from fastapi import HTTPException

from . import models, schema
from .adapters import ExchangeRatesAdapter


async def call_for_convert_currencies(call: schema.Call, database) -> models.CallModel:
    exchange_rates_adapter = ExchangeRatesAdapter()
    converted_value, status_code = await exchange_rates_adapter.get_converted_value(
        call
    )
    if not converted_value:
        raise HTTPException(status_code=status_code, detail="Undone!")

    new_call = models.CallModel(
        from_currency=call.from_currency,
        to_currency=call.to_currency,
        amount=call.amount,
        when=call.when,
        converted_value=converted_value,
    )
    database.add(new_call)
    database.commit()
    return new_call


async def get_all_calls(database) -> List[models.CallModel]:
    all_calls = database.query(models.CallModel).all()
    return all_calls
