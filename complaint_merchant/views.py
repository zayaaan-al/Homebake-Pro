from django.shortcuts import render
from complaint_merchant.models import ComplaintMerchant
from merchant.models import Merchant
from user.models import User
import datetime

# Create your views here.
def complaintmercnt(request):
    obb=User.objects.all()
    context={
        'x':obb
    }
    if request.method=="POST":
        ss=request.session['u_id']
        obj=ComplaintMerchant()
        obj.complaint=request.POST.get('cmp')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.user_id=request.POST.get('usr')
        obj.merchnt_id=ss
        obj.save()
    return render(request,'complaint_merchant/merchant_complaint.html', context)


def cmpandreply(request):
    obj=ComplaintMerchant.objects.all()
    context={
        'v':obj
    }
    return render(request,'complaint_merchant/merchant_add_view_cmplnt_post_reply.html',context)


def mer_reply(request,idd):
    if request.method == 'POST':
        obj = ComplaintMerchant.objects.get(complaint_id=idd)
        obj.reply = request.POST.get('rep')
        obj.save()
        return cmpandreply(request)
    return render(request,'complaint_merchant/merchant_reply.html')


def vw_reply(request):
    obj=ComplaintMerchant.objects.all()
    context={
        'r':obj
    }
    return render(request,'complaint_merchant/Merchant_view_reply.html',context)