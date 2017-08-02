from rest_framework import permissions
from.models import *
class AuthorizedOrgPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user=request.user
        if user.is_anonymous():
            return False
        elif request.data.get('donation_id',None) is not None:
            if DonationDetail.objects.filter(pk=request.data.get('donation_id',None)).exists():
                donationObject=DonationDetail.objects.filter(pk=request.data.get('donation_id',None))[:1].get()
                print("donation",donationObject.goods_id)
                goods_id=donationObject.goods_id.goods_id
                if GoodsDetail.objects.filter(pk=goods_id).exists():
                    goodsObject=GoodsDetail.objects.filter(pk=goods_id)[:1].get()
                    org_id=goodsObject.org_id.org_id
                    print("org",org_id)
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
            else:
                return True  
            
        return True
