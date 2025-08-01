from django.shortcuts import render
from product_customisation.models import ProductCustomisation
# Create your views here.
def product_customisation(request):
    if request.method=="POST":
        obj=ProductCustomisation()
        obj.cake_name=request.POST.get('prps')
        obj.flavour=request.POST.get('flvr')
        obj.wishes=request.POST.get('descrp')
        obj.layer=request.POST.get('lyr')
        obj.shape=request.POST.get('dsgn')
        obj.theme=request.POST.get('thme')
        obj.topper=request.POST.get('tppr')
        obj.details=request.POST.get('title')
        obj.image=request.POST.get('img')
        obj.quantity=request.POST.get('Qnty')
        obj.weight=request.POST.get('weit')
        obj.amount=request.POST.get('amnt')
        obj.status = 'pending'
        obj.product_id = 1
        obj.save()
    return render(request,'product_customisation/productcustomisation.html')

def mngcustordr(request):
    obj=ProductCustomisation.objects.all()
    context={
        'e':obj
    }
    return render(request,'product_customisation/mng_cust_order.html',context)

def updtcuststs(request,idd):
    if request.method=="POST":
        obj=ProductCustomisation.objects.get(product_customisation_id=idd)
        obj.status=request.POST.get('sts')
        obj.save()
        return vewandupdtcustordsts(request)
    return render(request,'product_customisation/Update_cust_Status.html')

def vewandupdtcustordsts(request):
    obj=ProductCustomisation.objects.all()
    context={
        'r':obj
    }
    return render(request,'product_customisation/view_and_update_cust_order_status.html',context)

def viwaprvordrcustpay(request):
    obj=ProductCustomisation.objects.all()
    context={
        'a':obj
    }
    return render(request,'product_customisation/View_aprv_ordr_cust_&pay.html',context)

def viwcstordrsts(request):
    obj=ProductCustomisation.objects.all()
    context={
        's':obj
    }
    return render(request,'product_customisation/view_cust_order_sts.html',context)

def viwprdtcst(request):
    obj=ProductCustomisation.objects.all()
    context={
        'd':obj
    }
    return render(request,'product_customisation/view_product_customisation.html',context)

def approve(request,idd):
    obj=ProductCustomisation.objects.get(product_customisation_id=idd)
    obj.status="Approved"
    obj.save()
    return mngcustordr(request)

def reject(request,idd):
    obj=ProductCustomisation.objects.get(product_customisation_id=idd)
    obj.status="Rejected"
    obj.save()
    return mngcustordr(request)