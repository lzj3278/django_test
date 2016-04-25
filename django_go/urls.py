#!/usr/bin/env python
# coding: utf-8
"""django_test URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django_go.views import index, list1, Add, Delete,AssetList,Login,register


urlpatterns = [

	url(r'^admin/', admin.site.urls),
	url(r'^index/', index),
	url(r'^list/(?P<name>\d*)/(?P<id>\d*)/', list1),  # 对应view里面的 值name 与view中的 name对应
	url(r'^list/(?P<name>\d*)/', list1, {'id': 22222}),  # 默认值

	# url(r'^juser/', include('django_go.urls')),
	# url(r'^jasset/', include('jasset.urls')),
	url(r'^add/(?P<name>\d*)/$', Add),
	url(r'^add/(?P<name>\w*)/$', Add),
	url(r'^delete/(?P<name>\w*)/$', Delete),
	url(r'^delete/(?P<name>\d*)/$', Delete),
	url(r'^assetlist/$', AssetList),
	url(r'^login/$', Login),
	url(r'^register/$', register),
]
