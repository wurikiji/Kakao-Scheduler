"""ogh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from kakao.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^keyboard*', keyboard),
    url(r'^message$', answer),
    url(r'^friend$', add_friend),
    url(r'^friend/(?P<user_key>.+)$', del_friend),
    url(r'^chat_room/(?P<user_key>.+)$', leaveRoom),
    url(r'^(?P<userKey>.+)$', loginWithKey),
]