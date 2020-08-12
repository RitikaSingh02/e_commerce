from django.conf.urls import url
from . import views

urlpatterns=[
   url(r'^email_verify/$',views.email,name="email"), 
]