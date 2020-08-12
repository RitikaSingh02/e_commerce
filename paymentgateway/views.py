from django.shortcuts import render
from django.http import JsonResponse
import json


def paytm(request):
    return render(request,'website/paytm.html')

def payment(request):
    if request.method == 'POST':
        
        return JsonResponse("allgood",safe=False)
