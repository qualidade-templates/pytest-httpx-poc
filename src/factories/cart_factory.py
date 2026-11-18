from __future__ import annotations

from dto.cart import CartProductItemDto, CreateCartRequestDto


class CartFactory:
    @staticmethod
    def with_product(product_id: str, quantity: int = 1) -> CreateCartRequestDto:
        return CreateCartRequestDto(
            produtos=[
                CartProductItemDto(
                    idProduto=product_id,
                    quantidade=quantity,
                )
            ]
        )
