from __future__ import annotations

import re

from clients.serverest_client import ServeRestClient
from dto.auth import LoginRequestDto
from factories.user_factory import UserFactory


def test_realiza_login_e_retorna_token_bearer(api: ServeRestClient) -> None:
    user = UserFactory.create_admin()

    create_response = api.users.create(user)
    assert create_response.status_code == 201
    created = create_response.json()
    assert created["message"] == "Cadastro realizado com sucesso"
    assert re.fullmatch(r"[a-zA-Z0-9]+", created["_id"])

    response = api.auth.login(
        LoginRequestDto(email=user.email, password=user.password)
    )

    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Login realizado com sucesso"
    assert re.fullmatch(r"Bearer\s.+", body["authorization"])
