from rest_framework import serializers
from Humane.models import *
from Humane.validators import *
from Humane.constants import *
from django.core.validators import validate_email
from django.contrib.auth import get_user_model
from django.db.models import Q

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
        if UserProfile.objects.filter(email=validated_data['email']).exists():
            if not UserProfile.objects.filter(mobile=validated_data['mobile']).exists():
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
            else:
                raise serializers.ValidationError({'Error':'Mobile number already exists'})
        else:
            raise serializers.ValidationError({'Error':'Email Id does not exists'})

class EditOrganisationDetailSerializer(serializers.ModelSerializer):
    org_reg_no = serializers.CharField(required=True)
    org_name = serializers.CharField(required=True)
    org_type = serializers.CharField(required=True)
    org_desc = serializers.CharField(required=True)
    org_logo = serializers.CharField(required=True)
    people_count = serializers.IntegerField(required=True)
    latitude=serializers.FloatField(required=False)
    longitude=serializers.FloatField(required=False)
    address = serializers.CharField(required=True)

    class Meta:
        model=UserProfile
        fields= 'org_reg_no','org_name','org_type','org_desc','org_logo','people_count','latitude','longitude','address',
    def create(self, validated_data):
        loggedin_user_id =  self.context['request'].user.id
        if OrganisationDetail.objects.filter(org_reg_no=validated_data['org_reg_no']).exists():
            organisationDetail = OrganisationDetail.objects.filter(org_reg_no=validated_data['org_reg_no']).get()
            organisationUser = OrganisationUserDetail.objects.filter(user_id=loggedin_user_id).get()

            if (organisationUser.organisation.org_id==organisationDetail.org_id):
                organisation=OrganisationDetail.objects.filter(org_reg_no=validated_data['org_reg_no'])[:1].get()
                organisation.org_name=validated_data.get('org_name',organisation.org_name)
                organisation.org_type=validated_data.get('org_type',organisation.org_type)
                organisation.org_desc=validated_data.get('org_desc',organisation.org_desc)
                organisation.org_logo=validated_data.get('org_logo',organisation.org_logo)
                organisation.people_count=validated_data.get('people_count',organisation.people_count)
                organisation.latitude=validated_data.get('latitude',organisation.latitude)
                organisation.longitude=validated_data.get('longitude',organisation.longitude)
                organisation.address=validated_data.get('address',organisation.address)
                organisation.save()
                return organisation

            else:
                raise serializers.ValidationError({'Error':'No permission to Edit'})
        else:
            raise serializers.ValidationError({'Error':'Org reg number does not exists'})

class OrgUserRegiserationSerializer(serializers.ModelSerializer):
    first_name =serializers.CharField(required=True,validators =[validate_name])
    email=serializers.EmailField(required=True)
    class Meta:
        model=UserProfile
        fields= ('first_name','email','role',)


class OrgDetailRegisterSerializer(serializers.ModelSerializer):
   user = OrgUserRegiserationSerializer(required=True,write_only=True,many=True)
   org_reg_no = serializers.CharField(required=True)
   org_name = serializers.CharField(required=True)
   address = serializers.CharField(required=True)
   org_type = serializers.CharField(required=True)
   org_desc = serializers.CharField(required=True)
   org_logo = serializers.CharField(required=True)
   people_count = serializers.IntegerField(required=True)

   class Meta:
       model=OrganisationDetail
       exclude = ('is_active',)

   def create(self, validated_data):
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
       organisationUserDetail=OrganisationUserDetail.objects.create(organisation=organisationDetail,user=userProfile)
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
        fields= 'first_name','email','mobile','latitude','longitude','address','role',

class DonationItemDetailSerializer(serializers.ModelSerializer):
    delivered_quantity = serializers.IntegerField(required=False,read_only = True)
    class Meta:
        model=DonationItemDetail
        exclude = ('delivered_quantity',)

class DonationDetailSerializer(serializers.ModelSerializer):
    donatingUser=DonatingUserDetailSerializer(required=True,write_only=True)
    donation_item_list=DonationItemDetailSerializer(many=True,required=False)
    promised_date = serializers.DateTimeField(required=True)
    delivered_date = serializers.DateTimeField(required=False,read_only = True)
    received_by = serializers.CharField(required=True,validators =[validate_address])
    is_volunteer_required = serializers.BooleanField(required=False)
    is_donation_completed = serializers.BooleanField(required=False,read_only = True)

    class Meta:
        model=DonationDetail
        exclude = ('delivered_date','is_donation_completed',)
    def create(self, validated_data):
        USER_MODEL=get_user_model()
        if not USER_MODEL.objects.filter(email= user['email']).exists():
           donatingUser['username']=donatingUser['email']
           userProfile=USER_MODEL.objects.create(**donatingUser)
           userProfile.set_password("12345678a")
           userProfile.save()
        else:
            raise serializers.ValidationError({'Error':'Email already exists'})
        return None

class GoodsItemDetailSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(required=True)
    posted_date = serializers.DateTimeField(required=True)
    deadline = serializers.DateTimeField(required=True)
    is_good_item_satisfied = serializers.BooleanField(required=False,read_only = True)
    class Meta:
        model=GoodsItemDetail
        exclude = ('is_good_item_satisfied','goods')

class GoodsDetailSerializer(serializers.ModelSerializer):
    goods_item_list=GoodsItemDetailSerializer(many=True,required=False)
    donation_list=DonationDetailSerializer(many=True,required=False,read_only=True)
    goods_txt_desc = serializers.CharField(required=False,validators =[validate_txt_desc])
    organisation=serializers.CharField(required=False,read_only=True)
    is_good_satisfied=serializers.BooleanField(required=False,read_only=True)
    class Meta:
        model=GoodsDetail
        fields = '__all__'
    def create(self, validated_data):
        items=validated_data.pop('goods_item_list')
        if OrganisationUserDetail.objects.filter(Q(user=self.context['request'].user.id)).exists():
            org=OrganisationUserDetail.objects.filter(user=self.context['request'].user.id)[:1].get()
            validated_data['organisation']=org.organisation
        else:
            raise serializers.ValidationError({'Error':'Invalid operation'})

        request_type=RequestTypeLookUp.objects.filter(Q(pk=goods_request_constant))[:1].get()
        validated_data['request']=request_type
        good=GoodsDetail.objects.create(**validated_data);
        for item in items:
            item['goods']=good
            GoodsItemDetail.objects.create(**item)
        return good

class ServiceDetailSerializer(serializers.ModelSerializer):
    goods_item_list=GoodsItemDetailSerializer(many=True,required=False)
    donation_list=DonationDetailSerializer(many=True,required=False,read_only=True)
    goods_txt_desc = serializers.CharField(required=False,validators =[validate_txt_desc])
    organisation=serializers.CharField(required=False,read_only=True)
    is_good_satisfied=serializers.BooleanField(required=False,read_only=True)
    class Meta:
        model=GoodsDetail
        fields = '__all__'
    def create(self, validated_data):
        items=validated_data.pop('goods_item_list')
        if OrganisationUserDetail.objects.filter(Q(user=self.context['request'].user.id)).exists():
            org=OrganisationUserDetail.objects.filter(user=self.context['request'].user.id)[:1].get()
            validated_data['organisation']=org.organisation
        else:
            raise serializers.ValidationError({'Error':'Invalid operation'})

        request_type=RequestTypeLookUp.objects.filter(Q(pk=service_request_constant))[:1].get()
        validated_data['request']=request_type
        good=GoodsDetail.objects.create(**validated_data);
        for item in items:
            item['goods']=good
            GoodsItemDetail.objects.create(**item)
        return good

class DonationCompletionSerialiser(serializers.ModelSerializer):
    donation_id=serializers.IntegerField(required=True)
    received_by=serializers.CharField(required=True)
    is_donation_completed=serializers.BooleanField(required=False,read_only=True)

    class Meta:
        model=DonationDetail
        fields=('donation_id','is_donation_completed','received_by')
    def create(self,validated_data):
        if DonationDetail.objects.filter(donation_id=validated_data['donation_id']).exists():
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
    is_good_satisfied=serializers.BooleanField(required=False,read_only=True)

    class Meta:
        model=GoodsDetail
        fields=('goods_id','is_good_satisfied')
    def create(self,validated_data):
        if GoodsDetail.objects.filter(goods_id=validated_data['goods_id']).exists():
            goods=GoodsDetail.objects.filter(goods_id=validated_data['goods_id'])[:1].get()
            goods.is_good_satisfied=True
            goods.save()
            return goods
        else:
            raise serializers.ValidationError({'Error':'Goods ID not found'})
        return None

class UserReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        exclude=('id','role',)

#Class OrgUSerDetailReadOnlySerializer(serializers.ModelSerializer):
#class Meta:
#        model=OrganisationUserDetail
#        exclude=('coordinator_id')

class OrgDetailReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganisationDetail
        exclude=('org_id')

class DonationItemDetailReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model=DonationItemDetail
        exclude=('donation_item_id',)

class DonationDetailReadOnlySerializer(serializers.ModelSerializer):
    donation_item_list=DonationItemDetailReadOnlySerializer(many=True,read_only=True)
    class Meta:
        model=DonationDetail
        exclude=('donation_id',)

class GoodsItemDetailReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model=GoodsItemDetail
        exclude=('goods_item_id',)

class GoodsDetailReadOnlySerializer(serializers.ModelSerializer):
    donations=DonationDetailReadOnlySerializer(many=True,read_only=True)
    goods_item_list=GoodsItemDetailReadOnlySerializer(many=True,read_only=True)
    #posted_by=OrgDetailReadOnlySerializer(read_only=True)

    class Meta:
        model=GoodsDetail
        exclude=('goods_id',)

