from __future__ import annotations

import pytest

from clients.serverest_client import ServeRestClient


@pytest.fixture
def api() -> ServeRestClient:
    client = ServeRestClient()
    yield client
    client.close()
