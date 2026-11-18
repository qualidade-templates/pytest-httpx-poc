from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class LoginRequestDto:
    email: str
    password: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class LoginResponseDto:
    message: str
    authorization: str
