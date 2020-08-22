from django.http import JsonResponse
import json
from django.shortcuts import render
import requests
from paytmchecksum import PaytmChecksum
from website.models import orders
import urllib.parse

def paytm(request):
    if request.method=="POST":
        data=json.loads(request.body)
        paytmParams = dict()
        paytmParams["body"] = {
            "requestType"   : "Payment",
            "mid"           : "IjxnIp43584314770202",
            "websiteName"   : "WEBSTAGING",
            "orderId"       : data['order_id'],
            "callbackUrl"   : "http://127.0.0.1:8000/payment/callback/",
            "txnAmount"     : {
                "value"     : data['amount'],
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
        orders.objects.filter(order_id=data['order_id']).update(trans_id=response["body"]["txnToken"])
        return JsonResponse(response,safe=False)

def payload_redirect(request,orderid):
    if request.method=="GET":
       
        context={
            "orderId":orderid,
            "tranId":orders.objects.filter(order_id=orderid).values('trans_id')
            }
    
        return render(request,'paytm.html',context)


#b'ORDERID=XkfFW&MID=IjxnIp43584314770202&TXNAMOUNT=1.00&CURRENCY=INR&STATUS=TXN_FAILURE&RESPCODE=501&RESPMSG=Your+payment+has+been+declined+by+your+bank.+Please+contact+your+bank+for+any+queries.+If+money+has+been+deducted+from+your+account%2C+your+bank+will+inform+us+within+48+hrs+and+we+will+refund+the+same&BANKTXNID=&CHECKSUMHASH=VubIZfHEjo8mf%2B9Q%2FeXTRS2thrRbZm07mO4M55vVoGPt6W9tH3JhFJdrKiK3iqWS5495gjn%2B%2BNKlky5iwYihcGt7OX%2Bv%2BfDkf2PUGW%2F2FoI%3D'
#<class 'bytes'>
def process_transaction(request):
    if request.method=="POST":
        paytmParams = dict()
        #print(request.body)#b'ORDERID=XkfFW&MID=IjxnIp43584314770202&TXNAMOUNT=1.00&CURRENCY=INR&STATUS=TXN_FAILURE&RESPCODE=501&RESPMSG=Your+payment+has+been+declined+by+your+bank.+Please+contact+your+bank+for+any+queries.+If+money+has+been+deducted+from+your+account%2C+your+bank+will+inform+us+within+48+hrs+and+we+will+refund+the+same&BANKTXNID=&CHECKSUMHASH=VubIZfHEjo8mf%2B9Q%2FeXTRS2thrRbZm07mO4M55vVoGPt6W9tH3JhFJdrKiK3iqWS5495gjn%2B%2BNKlky5iwYihcGt7OX%2Bv%2BfDkf2PUGW%2F2FoI%3D'
        # print(type(request.body))#<class 'bytes'>
        data=request.body
        string=data.decode('ASCII')
        print(string)
        result=string.split('&')
        orderid=result[0].split('=')[1]
        # print(orderid)
        # # body parameters
        paytmParams["body"] = {
            "mid" : "IjxnIp43584314770202",
            "orderId" : orderid}
        checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), "xviIzrLqoC%eSmQK")
        paytmParams["head"] = {
            "signature"	: checksum
        }
        post_data = json.dumps(paytmParams)

        # for Staging
        url = "https://securegw-stage.paytm.in/v3/order/status"

        # for Production
        # url = "https://securegw.paytm.in/v3/order/status"

        response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
        print(response)
        status=False
        if response['body']['resultInfo']['resultCode']=='01':
            orders.objects.filter(order_id=orderid).update(status="SUCCESS")
            status=True
            return render(request,"payment_status.html",{"status":status})
        else:
            orders.objects.filter(order_id=orderid).update(status="FAILED")
            return render(request,"payment_status.html",{"status":status})
               
        
