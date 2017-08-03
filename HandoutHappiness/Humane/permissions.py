from rest_framework import permissions
from.models import *

class AuthorizedOrgPermissionForDonationCompletion(permissions.BasePermission):
    def has_permission(self, request, view):
        user=request.user
        if user.is_anonymous():
            return False
        elif request.data.get('donation_id',None) is not None:
            if DonationDetail.objects.filter(pk=request.data.get('donation_id',None)).exists():
                donationObject=DonationDetail.objects.filter(pk=request.data.get('donation_id',None))[:1].get()
                goodsObject=donationObject.goods.goods_id
                if GoodsDetail.objects.filter(pk=goodsObject).exists():
                    goodsObject=GoodsDetail.objects.filter(pk=goodsObject)[:1].get()
                    organisationDetail=goodsObject.organisation.org_id

                    if OrganisationUserDetail.objects.filter(organisation=organisationDetail).exists():
                        organisationUserDetail = OrganisationUserDetail.objects.filter(organisation=organisationDetail)[:1].get()
                        organisationUser = organisationUserDetail.user
                        if(organisationUser.id == user.id):
                            return True
                        else:
                            return False
                    else:
                        return True
                else:
                    return True
            else:
                return True
        return True


class AuthorizedOrgPermissionForNeedCompletion(permissions.BasePermission):
    def has_permission(self, request, view):
        user=request.user
        if user.is_anonymous():
            return False
        elif request.data.get('goods_id',None) is not None:
            if GoodsDetail.objects.filter(pk=request.data.get('goods_id',None)).exists():
                goodsObject=GoodsDetail.objects.filter(pk=request.data.get('goods_id',None))[:1].get()
                organisationDetail=goodsObject.organisation.org_id

                if OrganisationUserDetail.objects.filter(organisation=organisationDetail).exists():
                    organisationUserDetail = OrganisationUserDetail.objects.filter(organisation=organisationDetail)[:1].get()
                    organisationUser = organisationUserDetail.user
                    if(organisationUser.id == user.id):
                print("Goods",goodsObject.goods_id)
                org_id=goodsObject.org_id.org_id
                if OrganisationUserDetail.objects.filter(pk=org_id).exists():
                    organisationUser = OrganisationUserDetail.objects.filter(pk=org_id)[:1].get()
                    coordinator_id = organisationUser.coordinator_id
                    if(coordinator_id==user.id):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return True
        return True

class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        SAFE_METHODS=['GET','HEAD']
        if  request.method in SAFE_METHODS:
            return True
        elif request.user.is_anonymous():
            return False
        else:
            return OrganisationUserDetail.objects.filter(user=request.user.id).exists()
        return False
