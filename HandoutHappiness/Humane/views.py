from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Humane.models import *
from Humane.serializers import *
from Humane.pagination import *
from Humane.filters import *
from .permissions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.db.models import Prefetch
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class OrganisationDetailRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = OrgDetailRegisterSerializer
    http_method_names = ['post', 'head']
    pagination_class = StandardResultsSetPagination
    queryset=OrganisationDetail.objects.all()


class EditUserDetailViewSet(viewsets.ModelViewSet):
    serializer_class = EditUserDetailSerializer
    http_method_names = ['post','get']
    pagination_class = StandardResultsSetPagination
    permission_classes=(IsAuthenticated,)
    def get_queryset(self):
       loggedin_user_id = self.request.user.id
       if UserProfile.objects.filter(id=loggedin_user_id).exists():
           return UserProfile.objects.filter(id=loggedin_user_id)
       else:
           return UserProfile.objects.all()

class EditOrganisationDetailViewSet(viewsets.ModelViewSet):
    serializer_class = EditOrganisationDetailSerializer
    http_method_names = ['post','get']
    pagination_class = StandardResultsSetPagination
    permission_classes=(IsAuthenticated,)
    def get_queryset(self):
        loggedin_user_id = self.request.user.id
        if OrganisationUserDetail.objects.filter(user=loggedin_user_id).exists():
           organisationUserDetail=OrganisationUserDetail.objects.filter(user_id=loggedin_user_id)[:1].get()
           return OrganisationDetail.objects.filter(pk=organisationUserDetail.organisation.org_id)
        else:
           return OrganisationDetail.objects.all()

class GoodsDetailViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsDetailSerializer
    http_method_names = ['get','post','head']
    pagination_class = StandardResultsSetPagination
    permission_classes=(CustomPermission,)
    filter_class = GoodsFilter
    def get_queryset(self):
       loggedin_user_id = self.request.user.id
       if OrganisationUserDetail.objects.filter(user=loggedin_user_id).exists():
           organisationUserDetail=OrganisationUserDetail.objects.filter(user_id=loggedin_user_id)[:1].get()
           organisationDetail=organisationUserDetail.organisation
           orgGoodsDetail = GoodsDetail.objects.filter(Q(organisation=organisationDetail)& Q(is_good_satisfied=False))
           return orgGoodsDetail
       else:
           return GoodsDetail.objects.filter(Q(is_good_satisfied=False))

class ServiceDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceDetailSerializer
    http_method_names = ['get','post','head']
    pagination_class = StandardResultsSetPagination
    permission_classes=(CustomPermission,)
    filter_class = GoodsFilter
    def get_queryset(self):
       loggedin_user_id = self.request.user.id
       if OrganisationUserDetail.objects.filter(user=loggedin_user_id).exists():
           organisationUserDetail=OrganisationUserDetail.objects.filter(user_id=loggedin_user_id)[:1].get()
           organisationDetail=organisationUserDetail.organisation
           orgGoodsDetail = GoodsDetail.objects.filter(Q(organisation=organisationDetail)& Q(is_good_satisfied=False))
           return orgGoodsDetail
       else:
           return GoodsDetail.objects.filter(Q(is_good_satisfied=False))

class GoodsItemDetailViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsItemDetailSerializer
    http_method_names = ['get', 'head']
    pagination_class = StandardResultsSetPagination
    queryset=GoodsItemDetail.objects.all()

class DonationDetailViewSet(viewsets.ModelViewSet):
    serializer_class = DonationDetailSerializer
    http_method_names = ['get', 'head']
    pagination_class = StandardResultsSetPagination
    queryset = DonationDetail.objects.all()

class DonationItemDetailViewSet(viewsets.ModelViewSet):
    serializer_class = DonationItemDetailSerializer
    http_method_names = ['get', 'head']
    pagination_class = StandardResultsSetPagination
    queryset=GoodsItemDetail.objects.all()

class DonationCompletionViewSet(viewsets.ModelViewSet):
    serializer_class = DonationCompletionSerialiser
    http_method_names = ['post', 'head','get']
    permission_classes = (AuthorizedOrgPermissionForDonationCompletion,)
    def get_queryset(self):
       loggedin_user_id = self.request.user.id
       if OrganisationUserDetail.objects.filter(user=loggedin_user_id).exists():
           organisationUserDetail=OrganisationUserDetail.objects.filter(user_id=loggedin_user_id)[:1].get()
           organisationDetail=organisationUserDetail.organisation
           orgGoodsDetail = GoodsDetail.objects.filter(organisation=organisationDetail)[:1].get()
           return DonationDetail.objects.filter(Q(goods=orgGoodsDetail)& Q(is_donation_completed=False))
       else:
           return DonationDetail.objects.filter(Q(is_donation_completed=False))

class NeedCompletionViewSet(viewsets.ModelViewSet):
    serializer_class = NeedCompletionSerialiser
    http_method_names = ['post', 'head','get']
    permission_classes = (AuthorizedOrgPermissionForNeedCompletion,)
    def get_queryset(self):
       loggedin_user_id = self.request.user.id
       if OrganisationUserDetail.objects.filter(user=loggedin_user_id).exists():
           organisationUserDetail=OrganisationUserDetail.objects.filter(user_id=loggedin_user_id)[:1].get()
           organisationDetail=organisationUserDetail.organisation
           return GoodsDetail.objects.filter(Q(organisation=organisationDetail)& Q(is_good_satisfied=False))
       else:
           return GoodsDetail.objects.filter(Q(is_good_satisfied=False))

class AllDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsDetailReadOnlySerializer
    http_method_names = ['get', 'head']
    pagination_class = StandardResultsSetPagination
    queryset=GoodsDetail.objects.all()

class GoodsItemDetailReadOnlyViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsItemDetailReadOnlySerializer
    http_method_names = ['get', 'head']
    queryset=GoodsItemDetail.objects.all()

class DonationDetailReadOnlyViewSet(viewsets.ModelViewSet):
    serializer_class = DonationDetailReadOnlySerializer
    http_method_names = ['get', 'head']
    queryset=DonationDetail.objects.all()

class DonationItemDetailReadOnlyViewSet(viewsets.ModelViewSet):
    serializer_class = DonationItemDetailReadOnlySerializer
    http_method_names = ['get', 'head']
    queryset=DonationItemDetail.objects.all()

class OrganisationDetailReadOnlyViewSet(viewsets.ModelViewSet):
    serializer_class = OrgDetailReadOnlySerializer
    http_method_names = ['get', 'head']
    queryset=OrganisationDetail.objects.all()


