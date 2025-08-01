# from django.conf.urls import url
from django.urls import re_path


from chat import views

urlpatterns=[
    re_path('nur/',views.con),
    re_path('con/(?P<idd>\w+)',views.cochat),

    re_path('usr/',views.std),
    re_path('std/(?P<idd>\w+)',views.stchat),

]