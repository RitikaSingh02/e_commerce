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
            request.session["email"] = data['email']
            request.session['password'] =data['password']
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
        
        return JsonResponse("yes",safe=False)

def logout(request):
    try:
        del request.session['email']
        del request.session['password']
        #The output will look like this and don’t worry if your cookie didn’t delete
        # because we use this method only to delete your data in the Django database and not the session ID and cookie itself.
        #you can check it by access_session funct it would raise an error coz no session will be there
        #to completely delete use flush()
       
    except:
        pass
    return JsonResponse("logout successfull",safe=False)

