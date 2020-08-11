from django.conf.urls import url
from . import views

urlpatterns=[
 #   url(r'^$',views.patients_list,name="patients_list"),

   url(r'^paytm/$',views.paytm,name="paytm"),
   url(r'^email/$',views.email,name="email"), 
   url(r'^product_details/$',views.product_details,name="verify_email"),
   url(r'^payment/$',views.payment,name="payment"), 
   url(r'^email_verify/$',views.email_verify,name="verify_email"),
   url(r'^otp_save/$',views.otp_save,name="otp_save"),
   url(r'^otp_verify/$',views.otp_verify,name="otp_verify"),
  #  url(r'^location/$',views.location,name="verify_email"),


]