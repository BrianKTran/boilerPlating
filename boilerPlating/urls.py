from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from boilerPlateApp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index.as_view(), name='index'),
    path('basicPost/', views.basicPost.as_view(), name='basicGet'),
    path('basicGet/', views.basicGet.as_view(), name='basicGet'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
