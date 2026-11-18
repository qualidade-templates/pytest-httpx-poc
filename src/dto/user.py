from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal

AdministradorFlag = Literal["true", "false"]


@dataclass(frozen=True)
class CreateUserRequestDto:
    nome: str
    email: str
    password: str
    administrador: AdministradorFlag

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class UserResponseDto:
    nome: str
    email: str
    password: str
    administrador: AdministradorFlag
    _id: str
