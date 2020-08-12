from django.conf.urls import url
from . import views

urlpatterns=[

   url(r'^otp_save/$',views.otp_save,name="otp_save"),
   url(r'^otp_verify/$',views.otp_verify,name="otp_verify"),

]