from django.urls import re_path
from merchant import views

urlpatterns=[
 re_path('merchant/',views.merchant),
 re_path('mngmernt/',views.mng_merch),
 re_path('accept/(?P<idd>\w+)',views.accept),
 re_path('reject/(?P<idd>\w+)',views.reject)





]