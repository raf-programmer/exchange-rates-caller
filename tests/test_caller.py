import random
from itertools import product
from unittest.mock import patch

import pytest
from httpx import AsyncClient

from caller.caller.models import CallModel
from conf_test_db import app, override_get_db
from tests.fixture_factories import CallDictFactory


@pytest.mark.asyncio
class TestCaller:
    @patch("caller.caller.adapters.requests")
    async def test_new_call(self, requests_mock):
        # given
        requests_mock.get.return_value.status_code = 200
        result_value = 123.45
        requests_mock.get.return_value.json.return_value = {"result": result_value}
        # when
        call_data = CallDictFactory.build()
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.post("/caller/", json=call_data)
        # then
        assert response.status_code == 201
        checked_keys = ("from_currency", "to_currency", "amount")
        for key in checked_keys:
            assert response.json()[key] == call_data[key]
        assert response.json()["converted_value"] == result_value

    async def test_get_list_calls(self, clean_db):
        # given
        list_calls_data = self.__given_list_calls()
        # when
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get(f"/caller/")
        # then
        assert response.status_code == 200
        checked_keys = ("from_currency", "to_currency", "amount", "converted_value")
        for i, key in product(range(3), checked_keys):
            assert response.json()[i][key] == list_calls_data[i][key]

    def __given_list_calls(self):
        list_calls = []
        for i in range(3):
            call_data = self.__given_call()
            list_calls.append(call_data)
        return list_calls

    def __given_call(self):
        call_data = CallDictFactory.build()
        call_data["converted_value"] = round(random.uniform(10, 700), 2)
        db = next(override_get_db())
        new_call = CallModel(**call_data)
        db.add(new_call)
        db.commit()
        return call_data
