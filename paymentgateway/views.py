from django.shortcuts import render
from django.http import JsonResponse
import json
from website.models import orders
# from . import paytm_checksum


def paytm_request(request):
    # if request.method=="POST":
    #     data=json.loads(request.body)
    #     order_id=data['order_id']
    #     paytmParams = dict()

    #     paytmParams["MID"]     = "IjxnIp43584314770202"
    #     paytmParams["ORDERID"] = order_id
    #     checksum = paytm_checksum.generateSignature(paytmParams, "xviIzrLqoC%eSmQK")
    #     verifyChecksum = paytm_checksum.verifySignature(paytmParams ,"xviIzrLqoC%eSmQK", checksum)
    #     paytmParams["CHECKSUMHASH"] = checksum

    #     post_data = json.dumps(paytmParams)
    #     print("generatesignature:"+str(checksum))
    #     print("verifychecksum"+str(verifyChecksum))

        # return JsonResponse(post_data,safe=False)
        pass
    
def payment(request):
    if request.method == 'POST':
        
        return JsonResponse("allgood",safe=False)
