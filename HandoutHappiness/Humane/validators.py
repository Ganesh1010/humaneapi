from django.core.validators import RegexValidator 
from Humane.models import *
from Humane.serializers import *

def validate_name(name):
    if not 3<len(name)<500:
      raise serializers.ValidationError("Enter minimum 3 characters")
    return name

def validate_mobile(mobile):
    if not len(mobile)== 10:
      raise serializers.ValidationError("Enter 10 digits")
    return mobile

def validate_address(address):
    if not len(address)< 1500:
      raise serializers.ValidationError("Character limit: max 1500")
    return address

def validate_txt_desc(txtdesc):
    if not len(txtdesc)< 4000:
      raise serializers.ValidationError("Character limit : max 4000")
    return txtdesc


