from __future__ import annotations

import httpx

from clients.http_client import IHttpClient, RequestOptions
from dto.user import CreateUserRequestDto


class UserClient:
    def __init__(self, http: IHttpClient) -> None:
        self._http = http

    def create(self, payload: CreateUserRequestDto) -> httpx.Response:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/usuarios",
                body=payload.to_dict(),
            )
        )
