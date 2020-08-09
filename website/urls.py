from django.conf.urls import url
from . import views

urlpatterns=[
 #   url(r'^$',views.patients_list,name="patients_list"),

   url(r'^paytm/$',views.paytm,name="paytm"),
   url(r'^email/$',views.email,name="email"), 
   url(r'^payment/$',views.payment,name="payment"), 
   url(r'^email_verify/$',views.email_verify,name="verify_email"),
   url(r'^sessions/$',views.sessions,name="verify_email"),
]