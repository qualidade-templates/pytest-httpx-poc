from __future__ import annotations

from clients.auth_client import AuthClient
from clients.cart_client import CartClient
from clients.http_client import IHttpClient
from clients.httpx_http_client import HttpxHttpClient
from clients.product_client import ProductClient
from clients.user_client import UserClient


class ServeRestClient:
    """Facade do domínio ServeRest.

    Agrupa os clients e centraliza a injeção do HttpClient.
    """

    def __init__(self, http_client: IHttpClient | None = None) -> None:
        self._http = http_client or HttpxHttpClient()
        self.users = UserClient(self._http)
        self.auth = AuthClient(self._http)
        self.products = ProductClient(self._http)
        self.carts = CartClient(self._http)

    def close(self) -> None:
        close = getattr(self._http, "close", None)
        if callable(close):
            close()

    def __enter__(self) -> ServeRestClient:
        return self

    def __exit__(self, *args) -> None:
        self.close()
