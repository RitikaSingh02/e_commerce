from django.http import JsonResponse
import json
from django.core.mail import send_mail
from django.template.loader import render_to_string



def email(request):
    if request.method=="POST":
        data=json.loads(request.body)
        emails=data['email']
        recipient={"emails":emails}

        msg_html = render_to_string('website/mail.html', recipient)
        send_mail(
        'AMAZING',
        'django mail',
        'ritikasingh001001@gmail.com',
        [emails],
        html_message=msg_html,
        fail_silently=False,#when set to false there will be a smtplib.SMTPException. These are the required fields and can not be empty.
        )   
        return JsonResponse("email rendered",safe=False)

