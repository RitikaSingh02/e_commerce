from django.conf.urls import url
from . import views

urlpatterns=[

   url(r'^paytm/$',views.paytm_request,name="paytm"),
   url(r'^payment/$',views.payment,name="payment"),

]