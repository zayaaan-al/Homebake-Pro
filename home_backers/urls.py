"""home_backers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from django.conf.urls import url,include
from django.urls import path, re_path, include

from temp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('chat/', include('chat.urls')),
    re_path('complaint_merchant/',include('complaint_merchant.urls')),
    re_path('login/',include('login.urls')),
    re_path('merchant/',include('merchant.urls')),
    re_path('normal_order/', include('normal_order.urls')),
    re_path('payment/', include('payment.urls')),
    re_path('product/',include('product.urls')),
    re_path('product_customisation/',include('product_customisation.urls')),
    re_path('registration_fee/',include('registration_fee.urls')),
    re_path('review/',include('review.urls')),
    re_path('user/',include('user.urls')),
    re_path('complaint_user/', include('complaint_user.urls')),
    re_path('temp/', include('temp.urls')),
    re_path('$',views.home)

]
