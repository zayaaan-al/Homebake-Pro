from django.shortcuts import render

# Create your views here.
def home(request):
    return  render(request,'temp/home.html')
def admin(request):
    return render(request,'temp/admin.html')
def merchant(request):
    return render(request,'temp/merchant.html')
def user(request):
    return render(request,'temp/user.html')

def admin_free(request):
    return render(request,'temp/admin_free.html')
def user_fee(request):
    return render(request,'temp/user_free.html')
def merchant_fre(request):
    return render(request,'temp/merchant_free.html')

def homeeee(request):
    return render(request,'temp/home_free.html')
