from django.urls import path
from billy.views import *
app_name='mobile'
urlpatterns=[
    path('billy/',billy,name='billy'),
]