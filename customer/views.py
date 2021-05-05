from django.shortcuts import render
from .models import CustomUser
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def my_login(request):
    if request.method == "POST":
        # print(request.body)
        data = json.loads(request.body)
        print(data)
        email = data['email']
        password = data['password']
        res = {}
        user = User.objects.filter(email=email).exists()
        # print(user)
        if user is False:
            # create a user
            uname = data['username']
            phone = data['phone']
            user = CustomUser.objects.create(
                user_name=uname,
                password=password,
                phone=phone,
                email=email
            )
            user = User.objects.create(
                username=uname,
                email=email,
                is_staff=1
            )
            user.set_password(password)
            user.save()
            res = {
                "msg": "user created",
                "sessionid": request.session
            }
            print(res)
            return JsonResponse("User created", safe=False)
        else:
            # print(request.META)

            # user = authenticate(username=username, password=password)
            uname = data['username']
            password = data['password']

            user = User.objects.get(username=uname)
            print(user)
            if user.is_active:

                user = authenticate(
                    request, username=uname, password=password)
                # print(user)
                # print(request.META)
                # print(user.is_authenticated)
                response = login(request, user)
                # print(request.META)
                # OBSERVATIONS OF THIS PRINT
                # at first time login no session id is created as it is  obvious that the same user has not been using that session
                # so now any api or any activity of the user that we want to be saved into that session is done below
                # so as soon this happens everything is stored in the django_sessions and now after u are login ans u print the META of your req
                # then it will have in what session you are logged in to django

                request.session['username'] = uname
                request.session['email'] = email
                # HTTP_COOKIE HEADER IS TOO DESTROYED as it was created only after the login is successfull
                # print(request.META['HTTP_COOKIE'].split('=')[1])
                sessiond = "gad13h48r5c12659myvq3ok5twrgi49q"

            user = CustomUser.objects.filter(email__contains=email, password__contains=password).filter(
                email=email, password=password).values()

            res = {"user": list(user), "sessionid": sessiond,
                   "msg": "YOU HAVE ALREADY SIGNED UP KINDLY PROCEED TO LOGIN"}
            return JsonResponse(res, safe=False)


def my_logout(request):
    # print(request.session['email']) ##email id is printed
    # print(request.META)  # session id is there under HTTP_COOKIE
    if 'HTTP_COOKIE' in request.META:
        logout(request)
        msg = "logged out successfully"
    else:
        msg = "wrong parameters"
    # no session id now
    # print(request.session['email']) # error as the sesion was terminated
    # print(request.META['HTTP_COOKIE'].split('=')[1])#HTTP_COOKIE HEADER IS TOO DESTROYED as it was created only after the login is successfull
    return JsonResponse(msg, safe=False)
