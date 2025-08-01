from django.urls import re_path
from review import views

urlpatterns=[
 re_path('review/',views.userreview),
 re_path('merchntvewrev/',views.merchntvewrevw),
 re_path('usrvewrev/',views.usrvewrvw),
]