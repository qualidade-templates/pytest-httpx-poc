from __future__ import annotations

import httpx

from clients.http_client import IHttpClient, RequestOptions
from dto.cart import CreateCartRequestDto


class CartClient:
    def __init__(self, http: IHttpClient) -> None:
        self._http = http

    def create(self, payload: CreateCartRequestDto, token: str) -> httpx.Response:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/carrinhos",
                body=payload.to_dict(),
                token=token,
            )
        )

    def get_by_id(self, cart_id: str) -> httpx.Response:
        return self._http.request(
            RequestOptions(
                method="GET",
                path=f"/carrinhos/{cart_id}",
            )
        )
