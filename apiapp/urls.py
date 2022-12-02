from django.urls import path
from apiapp.views import *

urlpatterns = [
    path('register/', userRegistration.as_view(), name='register'),
    path('smslog/', Smlogview.as_view(), name='smslog'),
    path('calllog/', Calllogview.as_view(), name='calllog'),
    path('location/', Locationview.as_view(), name='location'),
    path('contact/', Contactview.as_view(), name='contact'),
]
