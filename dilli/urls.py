from dilli.views import *
from django.urls import path
app_name='call'
urlpatterns=[
    path('dilli/',dilli,name='dilli'),
]