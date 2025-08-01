from django.urls import re_path
from payment import views

urlpatterns=[
 re_path('payment/(?P<idd>\w+)', views.payment),
 re_path('vewpay/', views.vewpay),
]