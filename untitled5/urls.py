"""untitled5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from .views import *
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^admin/', admin.site.urls),
    url(r'^acts/$', acts),
    url(r'^acts/(\d+)/$', acts),
    url(r'^$', index),
    url(r'^act/(?P<pk>[0-9]+)/$', act),
    url(r'^arbitrates/$', arbitrates),
    url(r'^createarbitrate/', new_arbitrate),
    url(r'^accounts/profile/', home),
    url(r'^createact/', new_act),
    url(r'^act/(?P<pk>[0-9]+)/change/', change_act),
]