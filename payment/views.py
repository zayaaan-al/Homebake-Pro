from django.shortcuts import render
from payment.models import Payment
# Create your views here.
def payment(request,idd):
    ss=request.session['u_id']
    if request.method=="POST":
        obj=Payment()
        obj.payment_method=request.POST.get('upi')
        obj.order_id=idd
        obj.price=request.POST.get('pc')
        obj.user_id=ss
        obj.save()

    return render(request, 'payment/payment.html')

def  vewpay(request):
    obj=Payment.objects.all()
    context={
        'q':obj
    }
    return render(request, 'payment/view_payment.html', context)