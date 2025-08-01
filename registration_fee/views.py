from django.shortcuts import render
from registration_fee.models import RegistrationFee
# Create your views here.
def registration_fee(request):
    if request.method=="POST":
        obj=RegistrationFee()
        # obj.amount=request.POST.get('Amount : 250')
        obj.amount="250"
        obj.save()
    return render(request,'registration_fee/registrationfee.html')

def viwregfee(request):
    obj=RegistrationFee.objects.all()
    context={
        'f':obj
    }
    return render(request,'registration_fee/view_registration_fee.html',context)