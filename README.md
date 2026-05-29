# Infraestrutura Web com Nginx Proxy Reverso + API REST

## Integrantes

| Nome |
|------|
| Ariane de Souza Franca
| Lívia Martins Bastos
| José Henrique Martins B. Silva
| Lamartine Almeida

---

## Descrição

Projeto Simula uma conexão Entre duas máquinas, configurada para ser intermediadora entre o clientes e o Servidor(Banckend). A primeira máquina tem o Backend e Nginx com a proxy Reversa. A segunda é o clientes. Não foi possível por conta da insfraestrura permitir ter 3 computadores para simular.

Fluxo:
Cliente (Seu PC) ──> VM 1 (Nginx / Proxy Reverso) e (Flask API + MySQL)

---

## Endereços IP das VMs

| Máquina | Função | IP |
|---------|--------|----|
| VM 1 | Nginx – Proxy Reverso | API Flask + MySQL | 192.168.56.102 |



## Estrutura do Repositório

```text
Projeto/
├── api/
│   ├── app.py
│   ├── database.py
│   └── requirements.txt
├── database/
│   └── schema.sql
├── docs/
│   └── rotas.md
├── nginx/
│   └── api
└── README.md
```

## Pré-requisitos

- Duas VMs com Ubuntu Server 22.04 ou Debian
- Rede configurada em modo Host-Only ou Bridge Caso for VM
- Acesso SSH ou terminal nas duas VMs

---

## Guia de Execução

### VM 2 — Banco de Dados (MySQL)

1. Instalar o MySQL:
sudo apt update
sudo apt install default-mysql-server -y

2. Criar usuário e banco:
sudo mysql -u root -p

CREATE DATABASE minha_api;
CREATE USER 'apiuser'@'localhost' IDENTIFIED BY 'senha123';
GRANT ALL PRIVILEGES ON minha_api.* TO 'apiuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;

3. Importar o schema:
sudo mysql -u root -p minha_api < database/schema.sql

### VM 2 — API REST (Flask)

1. Instalar dependências:
sudo apt install python3-pip python3-dev default-libmysqlclient-dev build-essential -y

2. Instalar dependências Python:
pip3 install -r api/requirements.txt

3. Iniciar a API:
python3 api/app.py

A API ficará disponível em http://192.168.56.102:3000

### VM 1 — Nginx (Proxy Reverso)

1. Instalar o Nginx:
sudo apt update
sudo apt install nginx -y

2. Copiar o arquivo de configuração:
sudo cp nginx/api /etc/nginx/sites-available/api

3. Ativar o Virtual Host:
sudo ln -s /etc/nginx/sites-available/api /etc/nginx/sites-enabled/api

4. Remover o Virtual Host padrão:
sudo rm -f /etc/nginx/sites-enabled/default

5. Testar e recarregar:
sudo nginx -t
sudo systemctl reload nginx

---

## Testando o fluxo completo

```texto
curl http://192.168.56.101/clientes

curl -X POST http://192.168.56.101/clientes \
  -H "Content-Type: application/json" \
  -d '{"nome": "João Silva", "email": "joao@email.com"}'

curl http://192.168.56.101/clientes/1

curl -X PUT http://192.168.56.101/clientes/1 \
  -H "Content-Type: application/json" \
  -d '{"nome": "João Atualizado", "email": "joao@email.com"}'

curl -X DELETE http://192.168.56.101/clientes/1

curl http://192.168.56.101/produtos

curl -X POST http://192.168.56.101/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Notebook", "preco": 3500.00, "estoque": 10}'

---
``
## Tecnologias Utilizadas

- Máquina 1: Ubuntu + Python 3 + Flask + MySQL
