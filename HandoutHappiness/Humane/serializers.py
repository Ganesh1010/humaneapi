from rest_framework import serializers
from Humane.models import *
from Humane.validators import *
from django.core.validators import validate_email
from django.contrib.auth import get_user_model

class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(required=True,write_only=True)
    first_name =serializers.CharField(required=True,validators =[validate_name])
    email=serializers.EmailField(required=True)
    mobile=serializers.CharField(required = False,validators =[validate_mobile])
    dob=serializers.DateField(required=False)
    latitude=serializers.FloatField(required=False)
    longitude=serializers.FloatField(required=False)
    address=serializers.CharField(required=False,validators =[validate_address])
    
    class Meta:
        model=UserProfile
        fields= 'password','first_name','email','mobile','dob','latitude','longitude','address','role',
    def create(self, validated_data):
        USER_MODEL=get_user_model()
        if not USER_MODEL.objects.filter(email=validated_data['email']).exists():
            if not USER_MODEL.objects.filter(mobile=validated_data['mobile']).exists():
                validated_data['username']=validated_data.get('email',validated_data.get('mobile',None))
                user=USER_MODEL.objects.create(**validated_data)
                user.set_password(validated_data.get('password',''))
                user.save()
                return user
        
            else:
                raise serializers.ValidationError({'Error':'Mobile already exists'})
        else:
            raise serializers.ValidationError({'Error':'Email already exists'})
    
            
class EditUserDetailSerializer(serializers.ModelSerializer):
    first_name =serializers.CharField(required=False,validators =[validate_name])
    email=serializers.EmailField(required=True)
    mobile=serializers.CharField(required=False,validators =[validate_mobile])
    dob=serializers.DateField(required=False)
    latitude=serializers.FloatField(required=False)
    longitude=serializers.FloatField(required=False)
    address=serializers.CharField(required=False)
    
    class Meta:
        model=UserProfile
        fields= 'first_name','email','mobile','dob','address','latitude','longitude',
    def create(self, validated_data):
        USER_MODEL=get_user_model()
        loggedin_user_id =  self.context['request'].user.id
        user=USER_MODEL.objects.filter(email=validated_data['email'])[:1].get()
        if user.id == loggedin_user_id:
            user.first_name=validated_data.get('first_name',user.first_name)
            user.mobile=validated_data.get('mobile',user.mobile)
            user.dob=validated_data.get('dob',user.dob)
            user.latitude=validated_data.get('latitude',user.latitude)
            user.longitude=validated_data.get('longitude',user.longitude)
            user.role=validated_data.get('role',user.role)
            user.save()
            return user
        
        else:
            raise serializers.ValidationError({'Error':'No permission to Edit'})
		

class OrgUserRegiserationSerializer(serializers.ModelSerializer):
    first_name =serializers.CharField(required=True,validators =[validate_name])
    email=serializers.EmailField(required=True)
    class Meta:
        model=UserProfile
        fields= 'first_name','email','role',


class OrgDetailRegisterSerializer(serializers.ModelSerializer):
   user = OrgUserRegiserationSerializer(required=True,write_only=True,many=True)
   org_reg_no = serializers.CharField(required=True)
   org_name = serializers.CharField(required=True)
   address = serializers.CharField(required=True)
   org_type = serializers.CharField(required=True)
   org_desc = serializers.CharField(required=True)
   org_logo = serializers.CharField(required=True)
   people_count = serializers.IntegerField(required=True)
   is_active = serializers.BooleanField(required=True)
   
   class Meta:
       model=OrganisationDetail
       fields = '__all__'

   def create(self, validated_data):
       print (validated_data)
       users=validated_data.pop('user')
       for user in users:
            USER_MODEL=get_user_model()
            if not USER_MODEL.objects.filter(email= user['email']).exists():
                user['username']=user['email']
                userProfile=USER_MODEL.objects.create(**user)
                userProfile.set_password("12345678a")
                userProfile.save()
            else:
                raise serializers.ValidationError({'Error':'Email already exists'})
       organisationDetail=OrganisationDetail.objects.create(**validated_data)
       organisationUserDetail=OrganisationUserDetail.objects.create(org_id=organisationDetail,user_id=userProfile)
       return organisationDetail


class DonatingUserDetailSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True,validators =[validate_name])
    email=serializers.EmailField(required=False)
    mobile=serializers.CharField(required = False,validators =[validate_mobile])
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    address = serializers.CharField(required=False,validators =[validate_address])
    class Meta:
        model=UserProfile
        fields= ('first_name','email','mobile','latitude','longitude','address','role',)

class DonationItemDetailSerializer(serializers.ModelSerializer):
    delivered_quantity = serializers.IntegerField(required=False,read_only = True)
    class Meta:
        model=DonationItemDetail
        exclude = ('delivered_quantity',)
    
class DonationDetailSerializer(serializers.ModelSerializer):
    donatingUser=DonatingUserDetailSerializer(required=True,write_only=True)
    donation_item_list=DonationItemDetailSerializer(many=True,required=True)
    delivered_date = serializers.DateTimeField(required=False,read_only = True)
    received_by = serializers.CharField(required=False,validators =[validate_address])
    is_volunteer_required = serializers.BooleanField(required=False)
    is_donation_completed = serializers.BooleanField(required=False,read_only = True)

    class Meta:
        model=DonationDetail
        exclude = ('delivered_date','is_donation_completed',)

    def create(self, validated_data):
        print (validated_data)
        user=validated_data.pop('donatingUser')
        USER_MODEL=get_user_model()
        if not USER_MODEL.objects.filter(email= user['email']).exists():
           user['username']=user['email']
           userProfile=USER_MODEL.objects.create(**user)
           userProfile.set_password("12345678a")
           userProfile.save()
        else:
            raise serializers.ValidationError({'Error':'Email already exists'})
        donationItemDetailList=validated_data.pop('donation_item_list')
        for donationItemDetail in donationItemDetailList:
            donationItemDetail['donation_id']=donationItemDetail['donation_id']
            donationItemDetail['goods_id']=donationItemDetail['goods_id']
            donationItemDetail['goods_item_id']=donationItemDetail['goods_item_id']
            donationItemDetail['promised_quantity']=donationItemDetail['promised_quantity']
            donationItemDetail['unit_id']=donationItemDetail['unit_id']
            DonationItemDetail.objects.create(**donationItemDetail)

        donationDetail=DonationDetail.objects.create(**validated_data)
        return donationDetail

class GoodsItemDetailSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(required=True)
    posted_date = serializers.DateTimeField(required=True)
    deadline = serializers.DateTimeField(required=True)
    is_good_item_satisfied = serializers.BooleanField(required=False,read_only = True)

    class Meta:
        model=GoodsItemDetail
        exclude = ('is_good_item_satisfied',)

class GoodsDetailSerializer(serializers.ModelSerializer):
    goods_item_list=GoodsItemDetailSerializer(many=True,required=False)
    donation_list=DonationDetailSerializer(many=True,required=False,read_only=True)
    is_good_satisfied = serializers.BooleanField(required=False,read_only = True)
    goods_txt_desc = serializers.CharField(required=False,validators =[validate_txt_desc])
    class Meta:
        model=GoodsDetail
        exclude = ('is_good_satisfied',)

class DonationCompletionSerialiser(serializers.ModelSerializer):
    donation_id=serializers.IntegerField(required=True)
    received_by=serializers.CharField(required=True)
    donation=DonationDetailSerializer(read_only=True,source="*")
    #delivered_quantity = serializers.IntegerField(required=True,write_only=True)
    class Meta:
        model=DonationDetail
        fields=('donation_id','donation','received_by')
    def create(self,validated_data):
        if DonationDetail.objects.filter(donation_id=validated_data['donation_id']).exists():
            print("present")
            donation=DonationDetail.objects.filter(donation_id=validated_data['donation_id'])[:1].get()
            donation.is_donation_completed=True
            donation.delivered_date=timezone.now()
            donation.received_by=validated_data.get('received_by',donation.received_by)
            #donation.delivered_quantity = validated_data.get('delivered_quantity',donation.delivered_quantity)
            donation.save()
            return donation
        else:
            raise serializers.ValidationError({'Error':'Donation ID not found'})
        return None

class NeedCompletionSerialiser(serializers.ModelSerializer):
    goods_id=serializers.IntegerField(required=True)
    goods_detail=GoodsDetailSerializer(read_only=True,source="*")
    #delivered_quantity = serializers.IntegerField(required=True,write_only=True)
    class Meta:
        model=GoodsDetail
        fields=('goods_id','goods_detail')
    def create(self,validated_data):
        if GoodsDetail.objects.filter(goods_id=validated_data['goods_id']).exists():
            goods=GoodsDetail.objects.filter(goods_id=validated_data['goods_id'])[:1].get()
            goods.is_good_satisfied=True
            goods.save()
            return goods
        else:
            raise serializers.ValidationError({'Error':'Goods ID not found'})
        return None


