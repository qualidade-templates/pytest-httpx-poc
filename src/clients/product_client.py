from __future__ import annotations

import httpx

from clients.http_client import IHttpClient, RequestOptions
from dto.product import CreateProductRequestDto


class ProductClient:
    def __init__(self, http: IHttpClient) -> None:
        self._http = http

    def create(self, payload: CreateProductRequestDto, token: str) -> httpx.Response:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/produtos",
                body=payload.to_dict(),
                token=token,
            )
        )
