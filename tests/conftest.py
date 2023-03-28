import pytest

from caller.caller.models import CallModel
from conf_test_db import override_get_db


@pytest.fixture(scope="function")
def clean_db():
    db = next(override_get_db())
    db.query(CallModel).delete()
    db.commit()
