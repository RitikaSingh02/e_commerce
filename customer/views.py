from django.shortcuts import render
from website.models import users
import json
from django.http import JsonResponse


def login(request):
    if request.method=="POST":
        data=json.loads(request.body)
        email=data['email']
        password=data['password']
        user=users.objects.filter(email__contains=email,password__contains=password).filter(email=email,password=password).values()
        if(user):
            return JsonResponse(list(user),safe=False)
        else:
            return JsonResponse("wrong",safe=False)
    

def signup(request):
    if request.method=="POST":
        data=json.loads(request.body)
        email=data['email']
        password=data['password']
        uname=data['username']
        phone=data['phone']
        user=users.objects.create(
            user_name=uname,
            password=password,
            phone=phone,
            email=email
        )
        request.session["email"] = data['email']
        return JsonResponse("yes",safe=False)

def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return JsonResponse("logout successfull",safe=False)


# Create your views here.
