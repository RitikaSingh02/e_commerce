from django.conf.urls import url
from . import views

urlpatterns=[ 
   url(r'^product_details/$',views.product_details,name="verify_email"),

]