from django.urls import re_path
from user import views

urlpatterns=[
  re_path('user/',views.user),
  re_path('manage/',views.mngusr),
  re_path('approve/(?P<idd>\w+)',views.approve),
  re_path('reject/(?P<idd>\w+)',views.reject)
]
