from django.urls import re_path  
from complaint_user import views

urlpatterns=[
    re_path('usrrly/(?P<idd>\w+)', views.usr_reply),
    re_path('usrvewcmprply/', views.comusrreply),
        re_path('user_complaint/', views.complaintuser),
    re_path('vwreply/', views.viw_reply),

]