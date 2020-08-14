import requests
import json
from website.models import orders
# import checksum generation utility
# You can get this utility from https://developer.paytm.com/docs/checksum/
import paytm_checksum

paytmParams = dict()

paytmParams["MID"]     = "IjxnIp43584314770202"
paytmParams["ORDERID"] = str(orders.id)

# Generate checksum by parameters we have
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
checksum = paytm_checksum.generateSignature(paytmParams, "xviIzrLqoC%eSmQK")
verifyChecksum = paytm_checksum.verifySignature(paytmParams ,"xviIzrLqoC%eSmQK", checksum)

print("generatesignature:"+str(checksum))
print("verifychecksum"+str(verifyChecksum))

paytmParams["CHECKSUMHASH"] = checksum

post_data = json.dumps(paytmParams)

# for Staging
url = "https://securegw-stage.paytm.in/order/status"

# for Production
# url = "https://securegw.paytm.in/order/status"

response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
print(response)
            
