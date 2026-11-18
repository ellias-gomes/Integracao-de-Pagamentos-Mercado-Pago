from flask import Flask, render_template, request
from mercado_pago_api import gerar_link

app = Flask(__name__)

@app.route("/")
def index():
    link_pagamento = gerar_link()
    return render_template("index.html", link_pagamento = link_pagamento)

@app.route("/success")
def success():
    # Extrair os parâmetros da URL
    collection_id = request.args.get('collection_id')
    collection_status = request.args.get('collection_status')
    payment_id = request.args.get('payment_id')
    status = request.args.get('status')
    external_reference = request.args.get('external_reference')
    payment_type = request.args.get('payment_type')
    merchant_order_id = request.args.get('merchant_order_id')
    preference_id = request.args.get('preference_id')
    site_id = request.args.get('site_id')
    processing_mode = request.args.get('processing_mode')
    merchant_account_id = request.args.get('merchant_account_id')
    return render_template("success.html", collection_id = collection_id, collection_status = collection_status, payment_id = payment_id, status = status, external_reference = external_reference, payment_type = payment_type, merchant_order_id = merchant_order_id,preference_id = preference_id, site_id = site_id, processing_mode = processing_mode, merchant_account_id = merchant_account_id)

@app.route("/failure")
def failure():
    collection_id = request.args.get('collection_id')
    collection_status = request.args.get('collection_status')
    payment_id = request.args.get('payment_id')
    status = request.args.get('status')
    external_reference = request.args.get('external_reference')
    payment_type = request.args.get('payment_type')
    merchant_order_id = request.args.get('merchant_order_id')
    preference_id = request.args.get('preference_id')
    site_id = request.args.get('site_id')
    processing_mode = request.args.get('processing_mode')
    merchant_account_id = request.args.get('merchant_account_id')
    return render_template("failure.html",  collection_id = collection_id, collection_status = collection_status, payment_id = payment_id, status = status, external_reference = external_reference, payment_type = payment_type, merchant_order_id = merchant_order_id,preference_id = preference_id, site_id = site_id, processing_mode = processing_mode, merchant_account_id = merchant_account_id)

if __name__ == "__main__":
    app.run()