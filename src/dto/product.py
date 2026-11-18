from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class CreateProductRequestDto:
    nome: str
    preco: int
    descricao: str
    quantidade: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class ProductResponseDto:
    nome: str
    preco: int
    descricao: str
    quantidade: int
    _id: str
