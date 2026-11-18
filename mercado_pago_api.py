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
            "success": "http://127.0.0.1:5000/success",
            "failure": "http://127.0.0.1:5000/failure",
            "pending": "http://127.0.0.1:5000/failure"
        },
        "auto_return": "all"
    }
    result = sdk.preference().create(payment_data, request_options)
    payment = result["response"]
    print(payment)
    return payment["init_point"]