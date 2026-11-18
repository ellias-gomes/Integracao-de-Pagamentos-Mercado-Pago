import os
import mercadopago

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def gerar_link():
    access_token = os.getenv("MERCADO_PAGO_ACCESS_TOKEN")
    if not access_token:
        raise ValueError("A variável de ambiente MERCADO_PAGO_ACCESS_TOKEN não está definida.")

    sdk = mercadopago.SDK(access_token)

    request_options = mercadopago.config.RequestOptions()
    request_options.custom_headers = {
        'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
    }

    base_url = os.getenv("BASE_URL", "http://127.0.0.1:5000").rstrip("/")

    payment_data = {
        "items": [
            {
                "id": "1",
                "title": "Camisa",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 259.99,
                "description": "Camisa super cara"
            }
        ],
        "back_urls": {
            "success": f"{base_url}/success",
            "failure": f"{base_url}/failure",
            "pending": f"{base_url}/failure"
        },
    }

    # A API do Mercado Pago rejeita auto_return quando as back_urls usam HTTP/localhost
    if base_url.startswith("https://"):
        payment_data["auto_return"] = "all"

    result = sdk.preference().create(payment_data, request_options)
    payment = result.get("response", {})
    if result.get("status", 0) >= 400 or "init_point" not in payment:
        raise RuntimeError(f"Erro ao criar preferência no Mercado Pago: {payment}")

    return payment["init_point"]