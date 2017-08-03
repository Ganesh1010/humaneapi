"""HandoutHappiness URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt import views as jwt_views
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^humane/', include('Humane.humaneurls')),
    url(r'^auth/login/', jwt_views.obtain_jwt_token, name='auth'),
    url(r'^verify/', jwt_views.verify_jwt_token),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^$', schema_view)
]
