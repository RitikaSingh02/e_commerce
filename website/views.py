from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import users,products,otp_table
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
        emails=data['email']
        recipient={"emails":emails}

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
                             to=[emails], body="django email")
        msg.attach_alternative(html_body, "text/html")
        msg.send()
        return JsonResponse("email rendered",safe=False)

def email_verify(request):
    if request.method=="GET":
       
        return JsonResponse("RMNBJH",safe=False)

def product_details(request):
    if request.method=="GET":
        product=products.objects.filter(status="available").values()
        return JsonResponse(list(product),safe=False)

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
# proceed with city