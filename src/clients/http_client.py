from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal, Protocol

import httpx

HttpMethod = Literal["GET", "POST", "PUT", "DELETE", "PATCH"]


@dataclass(frozen=True)
class RequestOptions:
    path: str
    method: HttpMethod = "GET"
    headers: dict[str, str] = field(default_factory=dict)
    body: Any = None
    token: str | None = None


class IHttpClient(Protocol):
    """Abstração do cliente HTTP (Dependency Inversion).

    Clients de domínio dependem desta interface, não do HTTPX diretamente.
    Retorna a Response para o teste aplicar asserts.
    """

    def request(self, options: RequestOptions) -> httpx.Response: ...
