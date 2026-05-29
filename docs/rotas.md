# Documentação das Rotas da API

Base URL: http://IP_DA_VM1/

## Clientes

| Método | Rota | Descrição | Body |
|--------|------|-----------|------|
| GET | /clientes | Lista todos os clientes | — |
| GET | /clientes/:id | Busca cliente por ID | — |
| POST | /clientes | Cria novo cliente | {"nome": "João", "email": "joao@email.com"} |
| PUT | /clientes/:id | Atualiza cliente | {"nome": "João", "email": "joao@email.com"} |
| DELETE | /clientes/:id | Remove cliente | — |

## Produtos

| Método | Rota | Descrição | Body |
|--------|------|-----------|------|
| GET | /produtos | Lista todos os produtos | — |
| GET | /produtos/:id | Busca produto por ID | — |
| POST | /produtos | Cria novo produto | {"nome": "Notebook", "preco": 3500.00, "estoque": 10} |
| PUT | /produtos/:id | Atualiza produto | {"nome": "Notebook", "preco": 3200.00, "estoque": 8} |
| DELETE | /produtos/:id | Remove produto | — |