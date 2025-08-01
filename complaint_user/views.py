from django.shortcuts import render
from complaint_user.models import ComplaintUser
from merchant.models import Merchant
import datetime
# Create your views here.
def complaintuser(request):
    ss=request.session['u_id']
    obb=Merchant.objects.all()
    context={
        'm':obb
    }
    if request.method=="POST":
        obj=ComplaintUser()
        obj.complaint=request.POST.get('cmpl')
        obj.date=datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.user_id = ss
        obj.merchant_id =request.POST.get('mer')
        obj.save()
    return render(request,'complaint_user/User_complaint.html',context)

def comusrreply(request):
    obj=ComplaintUser.objects.all()
    context={
        't':obj
    }
    return render(request,'complaint_user/User_add_view_complient_post_reply.html',context)

def usr_reply(request,idd):
    if request.method=='POST':
        obj=ComplaintUser.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('rp')
        obj.save()
        return comusrreply(request)
    return render(request,'complaint_user/User _Reply.html')

def viw_reply(request):
    obj=ComplaintUser.objects.all()
    contaxt={
        'y':obj
    }
    return render(request,'complaint_user/User_View_Reply.html',contaxt)
