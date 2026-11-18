from __future__ import annotations

import httpx

from clients.http_client import IHttpClient, RequestOptions
from dto.auth import LoginRequestDto


class AuthClient:
    def __init__(self, http: IHttpClient) -> None:
        self._http = http

    def login(self, payload: LoginRequestDto) -> httpx.Response:
        return self._http.request(
            RequestOptions(
                method="POST",
                path="/login",
                body=payload.to_dict(),
            )
        )
