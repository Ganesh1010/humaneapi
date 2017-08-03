from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class UserRoleLookUp(models.Model):
   user_role_id = models.AutoField(primary_key = True)
   user_role_type = models.CharField(max_length = 50)
   def __str__(self):
      return str(self.user_role_id)


class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=25, blank=True,null=True)
    dob=models.DateField(blank=True,null=True)
    latitude = models.FloatField(blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)
    address = models.CharField(max_length=500,blank=True,null=True)
    role = models.ForeignKey(UserRoleLookUp)
    def __str__(self):
        return str(self.id)

class OrganisationDetail(models.Model):
    org_id = models.AutoField(primary_key=True)
    org_reg_no = models.IntegerField()
    org_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=500)
    org_type = models.CharField(max_length=200)
    org_desc = models.CharField(max_length=500)
    org_logo = models.CharField(max_length=300)
    people_count = models.IntegerField()
    is_active = models.BooleanField()
    def __str__(self):
      return str(self.org_id)

class OrganisationUserDetail(models.Model):
    coordinator_id = models.AutoField(primary_key = True)
    organisation = models.ForeignKey(OrganisationDetail)
    user =  models.ForeignKey(UserProfile)
    def __str__(self):
      return str(self.coordinator_id)

class RequestTypeLookUp(models.Model):
    request_type_id = models.AutoField(primary_key = True)
    request_type_name = models.CharField(max_length=100)
    def __str__(self):
      return str(self.request_type_id)

class MainItemTypeLookUp(models.Model):
    main_item_id = models.AutoField(primary_key = True)
    main_item_name = models.CharField(max_length=100)
    request = models.ForeignKey(RequestTypeLookUp)
    def __str__(self):
      return str(self.main_item_id)


class SubItemTypeLookUp(models.Model):
    sub_item_id = models.AutoField(primary_key = True)
    sub_item_name = models.CharField(max_length=100)
    main_item = models.ForeignKey(MainItemTypeLookUp)
    def __str__(self):
      return str(self.sub_item_id)

class UnitLookUp(models.Model):
    unit_id = models.AutoField(primary_key = True)
    unit_name = models.CharField(max_length=100)
    def __str__(self):
      return str(self.unit_id)

class AllowedUnitLookUp(models.Model):
    allowed_unit_id = models.AutoField(primary_key = True)
    sub_item = models.ForeignKey(SubItemTypeLookUp)
    unit = models.ForeignKey(UnitLookUp)
    def __str__(self):
      return str(self.allowed_unit_id)

class GoodsDetail(models.Model):
    goods_id = models.AutoField(primary_key=True)
    organisation = models.ForeignKey(OrganisationDetail,related_name='org_detail')
    request = models.ForeignKey(RequestTypeLookUp)
    is_good_satisfied =models.BooleanField(default=False)
    main_item = models.ForeignKey(MainItemTypeLookUp)
    goods_txt_desc = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
      return str(self.goods_id)

class GoodsItemDetail(models.Model):
    goods_item_id = models.AutoField(primary_key = True)
    goods = models.ForeignKey(GoodsDetail,related_name='goods_item_list')
    quantity = models.IntegerField()
    posted_date =models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()
    sub_item = models.ForeignKey(SubItemTypeLookUp)
    is_good_item_satisfied = models.BooleanField(default=False)
    unit = models.ForeignKey(UnitLookUp)
    def __str__(self):
      return str(self.goods_item_id)

class DonationDetail(models.Model):
    donation_id = models.AutoField(primary_key = True)
    goods = models.ForeignKey(GoodsDetail,related_name='donation_list')
    promised_date = models.DateTimeField(default=timezone.now)
    delivered_date = models.DateTimeField(null=True,blank=True)
    received_by = models.CharField(max_length=250,null=True,blank=True)
    is_volunteer_required = models.BooleanField(default=False)
    is_donation_completed = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile)
    def __str__(self):
      return str(self.donation_id)

class DonationItemDetail(models.Model):
   donation_item_id = models.AutoField(primary_key = True)
   donation = models.ForeignKey(DonationDetail,related_name='donation_item_list')
   goods =  models.ForeignKey(GoodsDetail)
   goods_item = models.ForeignKey(GoodsItemDetail,related_name='goods_item_list')
   promised_quantity = models.IntegerField()
   delivered_quantity = models.IntegerField(null=True,blank=True)
   unit = models.ForeignKey(UnitLookUp)
   def __str__(self):
      return str(self.donation_item_id)
