from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CadastroResponseDto:
    message: str
    _id: str


@dataclass(frozen=True)
class MensagemResponseDto:
    message: str
