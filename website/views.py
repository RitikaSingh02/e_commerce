from django.http import JsonResponse
import json
from .models import products


def product_details(request):
    if request.method=="GET":
        product=products.objects.filter(status="available").values()
        return JsonResponse(list(product),safe=False)


