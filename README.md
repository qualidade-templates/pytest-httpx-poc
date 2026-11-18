# pytest-httpx-poc

Template de testes de API com **[Pytest](https://docs.pytest.org/)** + **[HTTPX](https://www.python-httpx.org/)**, usando a API pública [ServeRest](https://serverest.dev).

Faz parte da organização [`qualidade-templates`](https://github.com/qualidade-templates).

## O que tem aqui

Os mesmos fluxos do `pactum-js-poc` / `bruno-poc` / `insomnia-poc`, em código Python, com camadas separadas:

- **DTO** — contratos de request/response
- **Factory** — dados fake dinâmicos
- **HttpClient** — abstração (`IHttpClient`) + implementação HTTPX
- **Clients** — um por recurso (user, auth, product, cart); montam a request e devolvem a `Response`
- **Facade** — `ServeRestClient` agrupa tudo

Os clients **não** fazem assert. Status, payload e regras de negócio ficam nos testes.

Cobertura:

1. Cadastro de usuário
2. Login
3. Cadastro de produto
4. Carrinho (criar + buscar)
5. Fluxo E2E completo

## Estrutura

```
src/
  config/       # BASE_URL
  dto/
  factories/
  clients/      # HttpClient + clients de domínio + ServeRestClient
tests/
  conftest.py   # fixture ServeRestClient
  e2e/          # asserts e orquestração
```

## Como usar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # opcional — default já aponta para ServeRest
pytest
```

Só o E2E completo:

```bash
pytest tests/e2e/test_purchase_flow.py -k e2e
```

Exemplo de uso no teste:

```python
response = api.users.create(user)
assert response.status_code == 201
body = response.json()
assert body["message"] == "Cadastro realizado com sucesso"
```

## Environment

| Variável   | Default                   |
|------------|---------------------------|
| `BASE_URL` | `https://serverest.dev`   |

## Princípios usados

- **SRP** — client monta request; teste valida resposta
- **DIP** — clients de domínio dependem de `IHttpClient`, não do HTTPX
- **Facade** — `ServeRestClient` como ponto único de entrada
- **Factory** — payloads únicos por execução

## Repositórios relacionados

- [pactum-js-poc](https://github.com/qualidade-templates/pactum-js-poc) — mesmos fluxos em PactumJS + TypeScript
- [bruno-poc](https://github.com/qualidade-templates/bruno-poc) — mesmos fluxos no Bruno
- [insomnia-poc](https://github.com/qualidade-templates/insomnia-poc) — mesmos fluxos no Insomnia
- [postman-poc](https://github.com/qualidade-templates/postman-poc) — mesmos fluxos no Postman Native Git
