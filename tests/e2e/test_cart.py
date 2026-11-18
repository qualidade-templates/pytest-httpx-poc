from __future__ import annotations

import re

from clients.serverest_client import ServeRestClient
from dto.auth import LoginRequestDto
from factories.cart_factory import CartFactory
from factories.product_factory import ProductFactory
from factories.user_factory import UserFactory


def test_cadastra_carrinho_e_busca_por_id(api: ServeRestClient) -> None:
    user = UserFactory.create_admin()

    user_response = api.users.create(user)
    assert user_response.status_code == 201
    created_user = user_response.json()

    login_response = api.auth.login(
        LoginRequestDto(email=user.email, password=user.password)
    )
    assert login_response.status_code == 200
    authorization = login_response.json()["authorization"]

    product = ProductFactory.create(quantidade=20)
    product_response = api.products.create(product, authorization)
    assert product_response.status_code == 201
    created_product = product_response.json()

    cart_response = api.carts.create(
        CartFactory.with_product(created_product["_id"], 1),
        authorization,
    )
    assert cart_response.status_code == 201
    created_cart = cart_response.json()
    assert created_cart["message"] == "Cadastro realizado com sucesso"
    assert re.fullmatch(r"[a-zA-Z0-9]+", created_cart["_id"])

    get_response = api.carts.get_by_id(created_cart["_id"])
    assert get_response.status_code == 200
    cart = get_response.json()

    assert cart["_id"] == created_cart["_id"]
    assert cart["idUsuario"] == created_user["_id"]
    assert cart["produtos"][0]["idProduto"] == created_product["_id"]
    assert cart["quantidadeTotal"] == 1
    assert cart["precoTotal"] == product.preco
