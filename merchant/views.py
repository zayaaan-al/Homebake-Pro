from django.shortcuts import render
from merchant.models import Merchant
from login.models import  Login
# Create your views here.
def merchant(request):
    if request.method=="POST":
        obj=Merchant()
        obj.name=request.POST.get('name')
        obj.phone_number=request.POST.get('phn')
        obj.address=request.POST.get('adrs')
        obj.email=request.POST.get('email')
        obj.password=request.POST.get('psw')
        obj.location=request.POST.get('loc')
        obj.registration_id=1
        obj.status='pending'
        obj.save()

        # var = Login()
        # var.email = obj.email
        # var.password = obj.password
        # var.type = "merchant"
        # var.u_id = obj.merchant_id
        # var.save()

        ob=Login()
        ob.user_name=obj.name
        ob.password=obj.password
        ob.type="merchant"
        ob.u_id=obj.merchant_id
        ob.save()


    return render(request,'merchant/merchant.html')

def mng_merch(request):
    obj=Merchant.objects.all()
    context={
        'u':obj
    }
    return render(request,'merchant/manage_merchant.html',context)

def accept(request,idd):
    obj=Merchant.objects.get(merchant_id=idd)
    obj.status="Accepted"
    obj.save()
    return mng_merch(request)

def reject(request,idd):
    obj=Merchant.objects.get(merchant_id=idd)
    obj.status="Rejected"
    obj.save()
    return mng_merch(request)
