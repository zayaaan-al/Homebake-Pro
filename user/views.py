from django.shortcuts import render
from user.models import User
from login.models import Login
# Create your views here.
def user(request):
    if request.method == "POST":
        obj = User()
        obj.name=request.POST.get('Name')
        obj.phone_number=request.POST.get('phn')
        obj.address=request.POST.get('adrs')
        obj.phone_number=request.POST.get('phn')
        obj.email=request.POST.get('email')
        obj.password=request.POST.get('pswrd')
        obj.location=request.POST.get('lcn')
        obj.status='pending'
        obj.save()

        var=Login()
        var.user_name=obj.email
        var.password=obj.password
        var.type= "user"
        var.u_id=obj.user_id
        var.save()

    return render(request,'user/user.html')

def mngusr(request):
    obj=User.objects.all()
    context={
        'j':obj
    }
    return render(request,'user/manage_users.html',context)

def approve(request,idd):
    obj=User.objects.get(user_id=idd)
    obj.status="Approved"
    obj.save()
    return mngusr(request)

def reject(request,idd):
    obj=User.objects.get(user_id=idd)
    obj.status="Rejected"
    obj.save()
    return mngusr(request)