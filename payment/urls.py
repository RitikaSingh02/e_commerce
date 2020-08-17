from django.conf.urls import url
from . import views

urlpatterns=[

   url(r'^payment1/$',views.paytm,name="otp_save"),
#    url(r'^otp_verify/$',views.otp_verify,name="otp_verify"),

]