"""product_inventory_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve

from rest_framework.urlpatterns import format_suffix_patterns
from inventory import views

from graphene_django.views import GraphQLView

from product_inventory_manager.schema import schema

urlpatterns = [

    #url(r'^$', views.AngularAppView.as_view()),
    url(r'^$', serve,
        kwargs={'path': 'index.html'}),    
    url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s', permanent=False)),    
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    url(r'^products/$', views.product_list),
    url(r'^products/(?P<pk>[0-9]+)$', views.product_detail),
    url(r'^families/$', views.family_list.as_view()),
    url(r'^families/(?P<pk>[0-9]+)$', views.family_detail.as_view()),
    url(r'^locations/$', views.location_list.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)$', views.location_detail.as_view()),
    url(r'^transactions/$', views.transaction_list.as_view()),
    url(r'^transactions/(?P<pk>[0-9]+)$', views.transaction_detail.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)