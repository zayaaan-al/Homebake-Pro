from django.urls import re_path
from product import views

urlpatterns=[
 re_path('product/',views.product),
 re_path('vwprdtordr/',views.vewprdctandordr),
]