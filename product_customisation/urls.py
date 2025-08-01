from django.urls import re_path
from product_customisation import views

urlpatterns=[
 re_path('product_customisation/',views.product_customisation),
 re_path('mngcstordr/',views.mngcustordr),
 re_path('uptcststs/(?P<idd>\w+)',views.updtcuststs),
 re_path('vewupcstodrsts/',views.vewandupdtcustordsts),
 re_path('vewaprvordrcstpay/',views.viwaprvordrcustpay),
 re_path('vewcstordrsts/',views.viwcstordrsts),
 re_path('vewprdcst/',views.viwprdtcst),
 re_path('approve/(?P<idd>\w+)', views.approve),
 re_path('reject/(?P<idd>\w+)', views.reject)
]