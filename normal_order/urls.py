from django.urls import re_path
from normal_order import views

urlpatterns=[
 re_path('nrmlordr/(?P<idd>\w+)',views.normalorder),
 re_path('manage_order/',views.mngnororder),
 re_path('updtnrmlsts/(?P<idd>\w+)',views.upnorsts),
 re_path('vwupodrsts/',views.vwupdtr),
 re_path('aprve_normlorder/',views.aprvnrmlordr),
 re_path('listnrnlorsts/',views.nrmlordrsts),
 re_path('approve/(?P<idd>\w+)',views.approve),
 re_path('reject/(?P<idd>\w+)',views.reject)
]