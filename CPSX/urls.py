"""CPSX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from my_app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    #url(r'^about$', views.about, name='about'),
    #url(r'^compete$', views.compete, name='compete'),
    #url(r'^competitions$', views.competitions, name='competitions'),
    url(r'^guest$',views.guest,name='guest'),
    url(r'^loggedIn$',views.loggedIn,name='loggedIn'),
    url(r'^login', 'django.contrib.auth.views.login',name='login'),
    url(r'^register$', views.register,name='register'),
    #url(r'^accounts/',include('django.contrib.auth.urls')),
    #url(r'^',include('django.contrib.auth.urls')) # hashed out because using this logout logs the admin out
    url(r'^logout$', views.logout_view, name = 'loggedOut'),
    url(r'^contact/$', views.contact, name='contact'), # form to invite friends to participate
]

