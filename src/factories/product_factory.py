from __future__ import annotations

import random
import time

from dto.product import CreateProductRequestDto


class ProductFactory:
    @staticmethod
    def create(**overrides) -> CreateProductRequestDto:
        ts = int(time.time() * 1000)
        suffix = random.randint(0, 9_999)

        payload = CreateProductRequestDto(
            nome=f"Produto QA {ts}-{suffix}",
            preco=50 + (suffix % 450),
            descricao=f"Descricao dinamica gerada em {ts}",
            quantidade=10 + (suffix % 90),
        )

        if not overrides:
            return payload

        data = payload.to_dict()
        data.update(overrides)
        return CreateProductRequestDto(**data)
