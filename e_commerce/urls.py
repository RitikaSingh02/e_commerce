from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^amazing/', include('website.urls')),
    url(r'^amazing/user/', include('customer.urls')),
    url(r'^amazing/user/otp/', include('otpverification.urls')),
    url(r'^amazing/email/', include('emailverification.urls')),
    url(r'^payment/', include('payment.urls')),

]
