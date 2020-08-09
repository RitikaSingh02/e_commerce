from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import users
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



def paytm(request):
    return render(request,'website/paytm.html')

def payment(request):
    if request.method == 'POST':
        
        return JsonResponse("allgood",safe=False)

def email(request):
    if request.method=="POST":
        data=json.loads(request.body)
        email=data['email']
        recipient={"emails":email}

        # msg_html = render_to_string('website/mail.html', recipient)
        # send_mail(
        # 'AMAZING',
        # 'djando mail',
        # 'ritikasingh001001@gmail.com',
        # [email],
        # html_message=msg_html,
        # fail_silently=False,#when set to false there will be a smtplib.SMTPException. These are the required fields and can not be empty.
        # )   
        
        html_body = render_to_string("website/mail.html",recipient)

        msg = EmailMultiAlternatives(subject="AMAZING", from_email="ritikasingh001001@gmail.com",
                             to=[email], body="django email")
        msg.attach_alternative(html_body, "text/html")
        msg.send()
        return JsonResponse("email rendered",safe=False)

def email_verify(request):
    if request.method=="GET":
       
        return JsonResponse("RMNBJH",safe=False)

def sessions(request):
    if request.method=="POST":
        data=json.loads(request.body)
        request.session["email"] = data['email']
        return JsonResponse(request.session["email"],safe=False)
