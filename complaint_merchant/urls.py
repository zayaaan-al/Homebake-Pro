# from django.conf.urls import url
from django.urls import re_path

from complaint_merchant import views

urlpatterns=[
    re_path('complaint_merchant/',views.complaintmercnt),
    re_path('cmprep/',views.cmpandreply),
    re_path('merreply/(?P<idd>\w+)',views.mer_reply),
    re_path('mervewreply/',views.vw_reply),


]