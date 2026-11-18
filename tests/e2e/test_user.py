from __future__ import annotations

import re

from clients.serverest_client import ServeRestClient
from factories.user_factory import UserFactory


def test_cadastra_usuario_administrador_com_dados_dinamicos(api: ServeRestClient) -> None:
    payload = UserFactory.create_admin()

    response = api.users.create(payload)

    assert response.status_code == 201
    body = response.json()
    assert body["message"] == "Cadastro realizado com sucesso"
    assert re.fullmatch(r"[a-zA-Z0-9]+", body["_id"])
