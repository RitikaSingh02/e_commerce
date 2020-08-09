from django.conf.urls import url
from . import views

urlpatterns=[
   url(r'^login/$',views.login,name="login"),
   url(r'^signup/$',views.signup,name="login"), 
   url(r'^logout/$',views.logout,name="login"), 
   # url(r'^set/$',views.cookie_session,name="login"),
   # url(r'^del/$',views.cookie_delete,name="login"),
   # url(r'^access_session/$',views.access_session,name="login"),
    

]