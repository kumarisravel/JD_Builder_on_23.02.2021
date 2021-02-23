from django.conf.urls import include, url
from django.utils.translation import gettext_lazy as _
from .views import register
urlpatterns = [
    url(_(r'^login/$'),
        'django.contrib.auth.views.login',
        name='login'),
    url(_(r'^logout/$'),
        'django.contrib.auth.views.logout',
        name='logout'),
    url(_(r'^logout-then-login/$'),
        'django.contrib.auth.views.logout_then_login',
        name='logout_then_login'),
    url(_(r'^login/register/$'), register, name='register'),
]
