from django.conf.urls import url
from . import views

urlpatterns=[
   url(r'^email_render/$',views.email,name="email"), 
   url(r'^email_verify/(?P<emails>[\w\d@\.]+)/$',views.email_verify,name="email"),
]