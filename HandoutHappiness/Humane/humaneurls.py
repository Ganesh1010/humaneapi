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
from django.conf.urls import url
from django.contrib import admin
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'goodsDetail',views.GoodsDetailViewSet,'goodsDetail')
router.register(r'serviceDetail',views.ServiceDetailViewSet,'serviceDetail')
router.register(r'donationDetail',views.DonationDetailViewSet,'donationDetail')
router.register(r'orgDetailRegister',views.OrganisationDetailRegisterViewSet,'orgDetailRegister')
router.register(r'donationCompletion',views.DonationCompletionViewSet,'donationCompletion')
router.register(r'needCompletion',views.NeedCompletionViewSet,'needCompletion')
router.register(r'editUserDetail',views.EditUserDetailViewSet,'editUserDetail')
router.register(r'allDetail',views.AllDetailsViewSet,'allDetail')
router.register(r'allDonationDetail',views.DonationDetailReadOnlyViewSet,'allDonationDetail')


#router.register(r'goodsItemDetail',views.GoodsItemDetailViewSet,'goodsItemDetail')


urlpatterns = router.urls
