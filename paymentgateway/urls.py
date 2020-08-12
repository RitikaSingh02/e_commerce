from django.conf.urls import url
from . import views

urlpatterns=[

   url(r'^paytm/$',views.paytm,name="paytm"),
   url(r'^payment/$',views.payment,name="payment"),

]