from django.shortcuts import render
from multiprocessing import context
from os import stat
import pkgutil
from django.http import HttpResponse
from tkinter import NO
from urllib import request, response
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate
from apiapp.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
import io
import base64


# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class userRegistration(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            device_id = serializer.data.get('device_id')
            try:
                userdata = UserAccount.objects.get(
                    device_id=device_id)
                print(userdata)
            except:
                userdata = None
            if userdata is None:
                serializer = UserAccountSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({'status' : True, 'msg': 'Added Sucessfully', 'data' : serializer.data})
                
            
            elif userdata:
                request.session['device_id'] = userdata.device_id
                token = get_tokens_for_user(userdata)
                data = UserAccount.objects.get(device_id = device_id)
                serializer = UserAccountSerializer(data)
                return Response({'status' : True, 'token': token, 'msg': 'Login Success', 'data' : serializer.data}, status=status.HTTP_200_OK)
            
            else:
                return Response({'status' : False, 'msg': 'Device Id Invalid'}, status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self, request, id, format=None):
    #     request.session['device_id'] = userdata.device_id
    #     adressdata = UserAccount.objects.get(id=id)
    #     serializer = ItemSerializer(adressdata, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'msg': 'Updated  Successfully'}, status=status.HTTP_200_OK)
        
    
    




class Smlogview(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        device = request.session.get('device_id')
        mydevice = UserAccount.objects.get(device_id = device)
        serializer = SmsSerializers(
            data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save(user_id=mydevice)
            return Response({'status' : True, 'msg': 'Sms Logged Saved Successfully', "data" : serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status' : False,'msg': 'Sms Logged Saved Failed'})

  

class Calllogview(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        device = request.session.get('device_id')
        mydevice = UserAccount.objects.get(device_id = device)
        serializer = CallLogSerializers(
            data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save(user_id=mydevice)
            return Response({'status' : True,  'msg': 'Call Logged Saved Successfully', 'data' : serializer.data})
        else:
            return Response({'status' : False,'msg': 'Call Logged Saved Failed'})


class Locationview(APIView):

    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        device = request.session.get('device_id')
        mydevice = UserAccount.objects.get(device_id = device)
        serializer = UserLocationLogSerializers(
            data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save(user_id=mydevice)
            return Response({'status' : True, 'msg': 'Loaction Saved Successfully', 'data' : serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status' : False,'msg': 'Location Saved Failed'})

        


class Contactview(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        device = request.session.get('device_id')
        mydevice = UserAccount.objects.get(device_id = device)
        serializer = ContactSerializers(
            data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save(user_id=mydevice)
            return Response({'status' : True, 'msg': 'Contact Saved Successfully', 'data' : serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status' : False,'msg': 'Contact Saved Failed'})
    

