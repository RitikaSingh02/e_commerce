from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^amazing/', include('website.urls')),
    url(r'^amazing/user/', include('customer.urls')),
    url(r'^amazing/user/otp/', include('otpverification.urls')),
    url(r'^amazing/email/', include('emailverification.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^logout/', LogoutView.as_view()),
    url(r'', TemplateView.as_view(template_name="index.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# visit this url to know all the social acounts added
# http://127.0.0.1:8000/admin/socialaccount/socialaccount/
