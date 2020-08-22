from django.conf.urls import url
from . import views

urlpatterns=[

   url(r'^payment1/$',views.paytm,name="payment"),
   url(r'^payload/(?P<orderid>\w+)/$',views.payload_redirect,name="process"),
   url(r'^callback/$',views.process_transaction,name="process"),


]