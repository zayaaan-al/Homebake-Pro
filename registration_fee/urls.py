from django.urls import re_path
from registration_fee import views

urlpatterns=[
 re_path('registration_fee/',views.registration_fee),
 re_path('vewregfee/',views.viwregfee),
]