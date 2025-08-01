from django.shortcuts import render
from normal_order.models import NormalOrder
from product.models import Product
# Create your views here.
def normalorder(request,idd):
    ss=request.session['u_id']
    obj=Product.objects.get(product_id=idd)
    context={
        'x':obj
    }
    if request.method=="POST":
        obj=NormalOrder()
        obj.product_id=idd
        obj.quantity=request.POST.get('qnt')
        obj.status='pending'
        obj.amount=request.POST.get('amt')
        obj.wishes=request.POST.get('dsp')
        obj.weight=request.POST.get('wegt')
        obj.shape=request.POST.get('shp')
        obj.user_id=ss
        obj.save()
    return render(request, 'normal_order/Normal_order.html',context)

def mngnororder(request):
    obj=NormalOrder.objects.all()
    context={
        'u':obj
    }
    return render(request,'normal_order/Manage_normal_order.html',context)

def upnorsts(request,idd):
    obb=NormalOrder.objects.get(order_id=idd)
    context={
        'x':obb
    }
    if request.method=='POST':
        obj=NormalOrder.objects.get(order_id=idd)
        obj.status=request.POST.get('sts')
        obj.save()
        return vwupdtr(request)
    return render(request,'normal_order/Update_norml_Status.html', context)

def vwupdtr(request):
    obj=NormalOrder.objects.all()
    context={
        'i':obj
    }
    return render(request,'normal_order/view_and_update_normal_order_status.html',context)

def aprvnrmlordr(request):
    ss=request.session['u_id']
    obj=NormalOrder.objects.filter(user_id=ss,status="approved")
    context={
        'o':obj
    }
    return render(request,'normal_order/View_apprve_normal_order.html',context)

def nrmlordrsts(request):
    obj=NormalOrder.objects.all()
    context={
        'p':obj
    }
    return render(request,'normal_order/View_normal_Order_status.html',context)

def approve(request,idd):
    obj=NormalOrder.objects.get(order_id=idd)
    obj.status="Approved"
    obj.save()
    return mngnororder(request)

def reject(request,idd):
    obj=NormalOrder.objects.get(order_id=idd)
    obj.status="Rejected"
    obj.save()
    return mngnororder(request)


