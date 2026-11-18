from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class CartProductItemDto:
    idProduto: str
    quantidade: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class CreateCartRequestDto:
    produtos: list[CartProductItemDto]

    def to_dict(self) -> dict:
        return {
            "produtos": [item.to_dict() for item in self.produtos],
        }


@dataclass(frozen=True)
class CartProductDetailDto:
    idProduto: str
    quantidade: int
    precoUnitario: int


@dataclass(frozen=True)
class CartResponseDto:
    _id: str
    idUsuario: str
    precoTotal: int
    quantidadeTotal: int
    produtos: list[CartProductDetailDto]
