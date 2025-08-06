import pytest
from utils.api_util import RestfulBookerAPI

@pytest.fixture(scope="session")
def api_handle():
    client = RestfulBookerAPI()
    token = client.authenticate()
    return client

@pytest.fixture(scope="session")
def shared_booking_ids():
    return {}
