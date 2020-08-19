from django.http import JsonResponse
import json
from django.shortcuts import render
import requests
from paytmchecksum import PaytmChecksum
from website.models import orders

def paytm(request):
    if request.method=="POST":
        data=json.loads(request.body)
        paytmParams = dict()
        paytmParams["body"] = {
            "requestType"   : "Payment",
            "mid"           : "IjxnIp43584314770202",
            "websiteName"   : "WEBSTAGING",
            "orderId"       : data['order_id'],
            "callbackUrl"   : "https://merchant.com/callback",
            "txnAmount"     : {
                "value"     : "1.00",
                "currency"  : "INR",
            },
            "userInfo"      : {
                "custId"    : data['email'],
            },
        }

        checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), "xviIzrLqoC%eSmQK")
        orders.objects.create(

                order_id=data['order_id'],
                cust_mail=data['email'],
                checksum=str(checksum),
                cust_id=data['cust_id'],
                product_id=data['product_id']
        )
        paytmParams["head"] = {
            "signature"	: checksum
        }

        post_data = json.dumps(paytmParams)

        url = "https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid=IjxnIp43584314770202&orderId="+data['order_id']
        response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
        print(response)
        print(data['order_id'])

        return JsonResponse(response,safe=False)

def process_transaction(request):
    if request.method=="POST":
        data=json.loads(request.body)
        tran_id=data['tran_id']
        order_id=data['order_id']

        paytmParams = dict()

        paytmParams["body"] = {
            "requestType" : "NATIVE",
            "mid"         : "IjxnIp43584314770202",
            "orderId"     : data['order_id'],
            "paymentMode" : "CREDIT_CARD",
            "cardInfo"    : "|4111111111111111|111|122032",
            "authMode"    : "otp",
        }

        paytmParams["head"] = {
            "txnToken"    : tran_id
        }

        post_data = json.dumps(paytmParams)
        url = "https://securegw-stage.paytm.in/theia/api/v1/processTransaction?mid=IjxnIp43584314770202&orderId="+data['order_id']
        response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
        print(response)        
        return JsonResponse(response,safe=False)                 
        
