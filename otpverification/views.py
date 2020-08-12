from django.http import JsonResponse
import json
from website.models import otp_table

def otp_save(request):
    if request.method=="POST":
        data=json.loads(request.body)
        phone=data['phone']
        otp=data['otp']
        customer=otp_table.objects.create(
            phone=phone,
            otp=otp
        )
        return JsonResponse("otp saved success",safe=False)

def otp_verify(request):
    if request.method=="POST":
        data=json.loads(request.body)
        otp=data['otp']
        phone=data['phone']
        customer=otp_table.objects.filter(otp=otp,phone=phone,status="active").values()
        if(customer):
            customer=otp_table.objects.filter(otp=otp,phone=phone,status="active").update(status="inactive")
            return JsonResponse("correct",safe=False)
        else:
            return JsonResponse("wrong",safe=False)
