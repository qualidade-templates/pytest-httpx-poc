from __future__ import annotations

import re

from clients.serverest_client import ServeRestClient
from dto.auth import LoginRequestDto
from factories.cart_factory import CartFactory
from factories.product_factory import ProductFactory
from factories.user_factory import UserFactory


def test_fluxo_e2e_compra_completo(api: ServeRestClient) -> None:
    user = UserFactory.create_admin()
    product = ProductFactory.create(preco=150, quantidade=25)
    quantity_in_cart = 1

    user_response = api.users.create(user)
    assert user_response.status_code == 201
    created_user = user_response.json()
    assert created_user["message"] == "Cadastro realizado com sucesso"
    assert re.fullmatch(r"[a-zA-Z0-9]+", created_user["_id"])

    login_response = api.auth.login(
        LoginRequestDto(email=user.email, password=user.password)
    )
    assert login_response.status_code == 200
    login = login_response.json()
    assert login["message"] == "Login realizado com sucesso"
    assert re.fullmatch(r"Bearer\s.+", login["authorization"])

    product_response = api.products.create(product, login["authorization"])
    assert product_response.status_code == 201
    created_product = product_response.json()
    assert created_product["message"] == "Cadastro realizado com sucesso"
    assert re.fullmatch(r"[a-zA-Z0-9]+", created_product["_id"])

    cart_payload = CartFactory.with_product(created_product["_id"], quantity_in_cart)
    cart_response = api.carts.create(cart_payload, login["authorization"])
    assert cart_response.status_code == 201
    created_cart = cart_response.json()
    assert created_cart["message"] == "Cadastro realizado com sucesso"
    assert re.fullmatch(r"[a-zA-Z0-9]+", created_cart["_id"])

    get_response = api.carts.get_by_id(created_cart["_id"])
    assert get_response.status_code == 200
    cart = get_response.json()

    assert cart["_id"] == created_cart["_id"]
    assert cart["idUsuario"] == created_user["_id"]
    assert cart["quantidadeTotal"] == quantity_in_cart
    assert cart["precoTotal"] == product.preco * quantity_in_cart
    assert cart["produtos"][0]["idProduto"] == created_product["_id"]
    assert cart["produtos"][0]["quantidade"] == quantity_in_cart
