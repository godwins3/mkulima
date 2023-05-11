from app import mpesa, app




@app.route('/lipa-na-mpesa')

def lipa_na_mpesa(id):    
    access_token = mpesa.MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {'Authorization': 'Bearer %s' % access_token}
    mpesa_request = {
        'BusinessShortCode': mpesa.LipaNaMpesaPassword.business_short_code,   # org receiving funds
        'Password': mpesa.LipaNaMpesaPassword.decode_online_password,         # used to encrypt the request
        'Timestamp':mpesa.LipaNaMpesaPassword.lipa_time,                      # transaction time
        'TransactionType': 'CustomerPayBillOnline',
        'Amount': 1,                                                          # transaction amount
        'PartyA': int((current_user.phone).replace('+', '')),                 # MSISDN sending the funds
        'PartyB': mpesa.LipaNaMpesaPassword.business_short_code,               # org receiving the funds
        'PhoneNumber': int((current_user.phone).replace('+', '')),            # MSISDN sending the funds
        'CallBackURL': 'https://sandbox.safaricom.co.ke/mpesa/',
        'AccountReference': 'primashop',
        'TransactionDesc': 'testing stk push for ecommerce app'
    }
    try:
        response = requests.post(api_url, json=mpesa_request, headers=headers)
        print(response.text, f'\n\nStatus: {response.status_code}')

        # Update payment status in database
        product = PurchasedProducts.query.filter_by(id=id).first_or_404()
        product.payment_status = True
        db.session.commit()
        flash(f'{product.name} paid for.')

        # Send airtime after purchase
        send_airtime()

    except Exception as e:
        print(f'Error: \n\n {e}')    
    return redirect(url_for('dashboard_customer'))
