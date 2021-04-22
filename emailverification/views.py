from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import UserEmail
from django.core.mail import send_mail
from django.template.loader import render_to_string


def email(request):
    if request.method == "POST":
        data = json.loads(request.body)
        emails = data['email']
        recipient = {"emails": emails}

        msg_html = render_to_string('email/mail.html', recipient)
        send_mail(
            'AMAZING',
            'django mail',
            'ritikasingh001001@gmail.com',
            [emails],
            html_message=msg_html,
            # when set to false there will be a smtplib.SMTPException. These are the required fields and can not be empty.
            fail_silently=False,
        )

        UserEmail.objects.create(
            email=data['email']
        )
        return JsonResponse("email rendered", safe=False)


def email_verify(request, emails):
    if request.method == "GET":
        UserEmail.objects.filter(email=emails).update(status="verified")
        return render(request, 'email/verified.html', {"email": emails})


def email_status(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data['email']
        status = UserEmail.objects.filter(status="rendered").values()
        if(status):
            return JsonResponse("rendered", safe=False)
        else:
            return JsonResponse("verified", safe=False)
