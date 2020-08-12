
import requests
import json

# import checksum generation utility
# You can get this utility from https://developer.paytm.com/docs/checksum/
import PaytmChecksum

paytmParams = dict()

paytmParams["MID"]     = "YOUR_MID_HERE"
paytmParams["ORDERID"] = "ORDERID_98765"

# Generate checksum by parameters we have
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
checksum = PaytmChecksum.generateSignature(paytmParams, "YOUR_MERCHANT_KEY")

paytmParams["CHECKSUMHASH"] = checksum

post_data = json.dumps(paytmParams)

# for Staging
url = "https://securegw-stage.paytm.in/order/status"

# for Production
# url = "https://securegw.paytm.in/order/status"

response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
print(response)
            
