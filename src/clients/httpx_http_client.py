from __future__ import annotations

import httpx

from clients.http_client import RequestOptions
from config.env import env


class HttpxHttpClient:
    """Implementação HTTPX de IHttpClient."""

    def __init__(
        self,
        base_url: str | None = None,
        timeout: float = 20.0,
        client: httpx.Client | None = None,
    ) -> None:
        self._owns_client = client is None
        self._client = client or httpx.Client(
            base_url=base_url or env.base_url,
            timeout=timeout,
            headers={"Accept": "application/json"},
        )

    def request(self, options: RequestOptions) -> httpx.Response:
        headers = {
            **({"Content-Type": "application/json"} if options.body is not None else {}),
            **({"Authorization": options.token} if options.token else {}),
            **options.headers,
        }

        return self._client.request(
            method=options.method,
            url=options.path,
            headers=headers,
            json=options.body,
        )

    def close(self) -> None:
        if self._owns_client:
            self._client.close()

    def __enter__(self) -> HttpxHttpClient:
        return self

    def __exit__(self, *args) -> None:
        self.close()
