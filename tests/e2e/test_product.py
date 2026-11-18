from __future__ import annotations

import re

from clients.serverest_client import ServeRestClient
from dto.auth import LoginRequestDto
from factories.product_factory import ProductFactory
from factories.user_factory import UserFactory


def test_cadastra_produto_autenticado_como_administrador(api: ServeRestClient) -> None:
    user = UserFactory.create_admin()

    create_user = api.users.create(user)
    assert create_user.status_code == 201

    login_response = api.auth.login(
        LoginRequestDto(email=user.email, password=user.password)
    )
    assert login_response.status_code == 200
    authorization = login_response.json()["authorization"]

    product = ProductFactory.create()
    response = api.products.create(product, authorization)

    assert response.status_code == 201
    body = response.json()
    assert body["message"] == "Cadastro realizado com sucesso"
    assert re.fullmatch(r"[a-zA-Z0-9]+", body["_id"])
