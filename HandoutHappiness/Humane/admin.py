from django.contrib import admin
from .models import *
admin.site.site_header="Humane"

@admin.register(UserRoleLookUp)
class UserRoleLookUpAdminModel(admin.ModelAdmin):
   list_display =('user_role_id','user_role_type')

@admin.register(UserProfile)
class UserProfileAdminModel(admin.ModelAdmin):
   list_display =('id','email','first_name','last_name')

@admin.register(GoodsDetail)
class GoodsDetailAdminModel(admin.ModelAdmin):
   list_display =('goods_id','org_id','request_type','main_item_name','is_good_satisfied')

@admin.register(GoodsItemDetail)
class GoodsItemDetailAdminModel(admin.ModelAdmin):
   list_display =('sub_item_id','quantity','goods_id')

@admin.register(MainItemTypeLookUp)
class MainItemTypeLookUpAdminModel(admin.ModelAdmin):
   list_display =('main_item_id','main_item_name','request_type')

@admin.register(SubItemTypeLookUp)
class SubItemTypeLookUpAdminModel(admin.ModelAdmin):
   list_display =('sub_item_id','sub_item_name','main_item_name')

@admin.register(UnitLookUp)
class UnitLookUpAdminModel(admin.ModelAdmin):
   list_display =('unit_id','unit_name')

@admin.register(AllowedUnitLookUp)
class AllowedUnitLookUpAdminModel(admin.ModelAdmin):
   list_display =('allowed_unit_id','sub_item_id','unit_id')

@admin.register(RequestTypeLookUp)
class RequestTypeLookUpAdminModel(admin.ModelAdmin):
   list_display =('request_type_id','request_type_name')

@admin.register(OrganisationUserDetail)
class OrganisationUserDetailAdminModel(admin.ModelAdmin):
   list_display =('coordinator_id','user_id','org_id')

@admin.register(OrganisationDetail)
class OrganisationDetailAdminModel(admin.ModelAdmin):
   list_display =('org_id','org_name','is_active')

@admin.register(DonationDetail)
class DonationDetailAdminModel(admin.ModelAdmin):
   list_display =('donation_id','goods_id','user_id','is_donation_completed')

@admin.register(DonationItemDetail)
class DonationItemDetailAdminModel(admin.ModelAdmin):
   list_display =('donation_item_id','goods_item_id','promised_quantity','unit_id')
