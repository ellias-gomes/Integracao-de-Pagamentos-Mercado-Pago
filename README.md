# Integração de Pagamentos Mercado Pago

Protótipo em Flask para geração de links de pagamento (Checkout Pro) e tratamento de retornos utilizando a API oficial do Mercado Pago.

## Funcionalidades

- **Página inicial (`/`)**: Gera dinamicamente um link de pagamento para um item de exemplo e exibe o botão de checkout.
- **Retorno de sucesso (`/success`)**: Recebe e exibe os parâmetros retornados pelo Mercado Pago após a aprovação do pagamento (`collection_id`, `payment_id`, `status`, `merchant_order_id`, etc.).
- **Retorno de falha/pendência (`/failure`)**: Recebe e exibe os parâmetros de retorno caso o pagamento falhe ou fique pendente.

## Estrutura do Projeto

```text
.
├── main.py               # Servidor web Flask e definição das rotas
├── mercado_pago_api.py   # Integração com o SDK do Mercado Pago para criar preferências
├── templates/
│   ├── index.html        # Página inicial com o botão de compra
│   ├── success.html      # Página de confirmação de pagamento
│   └── failure.html      # Página de falha/pendência no pagamento
├── .env.example          # Modelo de variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo Git
└── README.md             # Documentação do projeto
```

## Tecnologias e Dependências

- **Python 3**
- **Flask** (`flask`)
- **Mercado Pago SDK** (`mercadopago`)
- **Python-Dotenv** (`python-dotenv`, opcional para carregar o arquivo `.env`)

## Configuração

1. Instale as dependências necessárias:
   ```bash
   pip install flask mercadopago python-dotenv
   ```

2. Configure o seu Access Token do Mercado Pago no arquivo `.env` (use `.env.example` como base):
   ```bash
   cp .env.example .env
   ```
   Edite o `.env` e informe sua credencial:
   ```env
   MERCADO_PAGO_ACCESS_TOKEN=seu_access_token_aqui
   ```

## Como Executar

1. Inicie o servidor Flask:
   ```bash
   python3 main.py
   ```
2. Acesse no navegador: `http://127.0.0.1:5000`
