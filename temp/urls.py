from django.urls import re_path
from temp import views

urlpatterns=[
    re_path('home/',views.home),
    re_path('admin/',views.admin),
    re_path('merchant/',views.merchant),
    re_path('user/',views.user),
    re_path('admin_free/', views.admin_free),
    re_path('user_fee/', views.user_fee),
    re_path('merchant_freeee/', views.merchant_fre),
    re_path('homeeee/', views.homeeee),

]