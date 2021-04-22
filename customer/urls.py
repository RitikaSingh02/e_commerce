from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.my_login, name="login"),
    # url(r'^signup/$',views.signup,name="login"),
    url(r'^logout/$', views.my_logout, name="login"),
]
