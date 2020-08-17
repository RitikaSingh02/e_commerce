from django.http import JsonResponse
import json
from django.shortcuts import render

def paytm(request):
    # More Details: https://developer.paytm.com/docs/checksum/#python
    if request.method=="POST":

        data=json.loads(request.body)

        import requests
        

        from paytmchecksum import PaytmChecksum

        # Generate Checksum via Hash/Array
        # initialize an Hash/Array
        paytmParams = {}

        paytmParams["MID"] = "IjxnIp43584314770202"
        paytmParams["ORDERID"] = data["order_id"]

        # Generate checksum by parameters we have
        # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        paytmChecksum = PaytmChecksum.generateSignature(paytmParams, "xviIzrLqoC%eSmQK")
        verifyChecksum = PaytmChecksum.verifySignature(paytmParams, "xviIzrLqoC%eSmQK",paytmChecksum)

        print("generateSignature Returns:" + str(paytmChecksum))
        print("verifySignature Returns:" + str(verifyChecksum))

        # Generate Checksum via String
        # initialize JSON String
        
        # body = "{\"mid\":\"IjxnIp43584314770202\",\"orderId\":\"123\"}"
        body="{\"mid\":\"IjxnIp43584314770202\",\"orderId\":"+data['order_id']+"\"}"

        # Generate checksum by parameters we have
        # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        paytmChecksum = PaytmChecksum.generateSignature(body, "xviIzrLqoC%eSmQK")
        verifyChecksum = PaytmChecksum.verifySignature(body, "xviIzrLqoC%eSmQK", paytmChecksum)

        print("generateSignature Returns:" + str(paytmChecksum))
        print("verifySignature Returns:" + str(verifyChecksum))

        context={
            "mid":"IjxnIp43584314770202",
            "orderid":data['order_id'],
            "email":data['email'],
            "amount":data['amount']

        }

        return JsonResponse(context,safe=False)
