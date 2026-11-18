from __future__ import annotations

import random
import time

from dto.user import CreateUserRequestDto


class UserFactory:
    @staticmethod
    def create_admin(**overrides) -> CreateUserRequestDto:
        ts = int(time.time() * 1000)
        suffix = random.randint(0, 99_999)

        payload = CreateUserRequestDto(
            nome=f"Usuario QA {ts}",
            email=f"usuario.{ts}.{suffix}@qa.com.br",
            password=f"Senha@{suffix}",
            administrador="true",
        )

        if not overrides:
            return payload

        data = payload.to_dict()
        data.update(overrides)
        return CreateUserRequestDto(**data)
