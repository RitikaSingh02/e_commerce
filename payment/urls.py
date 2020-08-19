from django.conf.urls import url
from . import views

urlpatterns=[

   url(r'^payment1/$',views.paytm,name="payment"),
    url(r'^process/$',views.process_transaction,name="process"),


]