from asyncore import write
from dataclasses import field, fields
from rest_framework import serializers
from apiapp.models import UserAccount, SmsLog, CallLog, UserLocation, Contact
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import base64
from django.contrib.auth.hashers import make_password

# UserAccount
class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['device_id', 'name', 'email']

    def create(self, validate_data):
        return UserAccount.objects.create(**validate_data)
    


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['device_id']
        


# SmsLog
class SmsSerializers(serializers.ModelSerializer):

    class Meta:
        model = SmsLog
        fields = ['user_id', 'from_sms', 'body',  'time_date']

    def create(self, validate_data):
        return SmsLog.objects.bulk_create(**validate_data)

# Callog
class CallLogSerializers(serializers.ModelSerializer):

    class Meta:
        model = CallLog
        fields = ['user_id','from_call', 'time_date',  'call_duration', 'call_type']

    def create(self, validate_data):
        return SmsLog.objects.create(**validate_data)


# Userlocation
class UserLocationLogSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserLocation
        fields = ['user_id','long', 'lat',  'TimeStamp', 'Address']

    def create(self, validate_data):
        return UserLocation.objects.create(**validate_data)


# Contact
class ContactSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserLocation
        fields = ['user_id','name', 'number']

    def create(self, validate_data):
        return Contact.objects.create(**validate_data)