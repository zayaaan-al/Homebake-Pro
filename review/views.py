from django.shortcuts import render
from review.models import Review

# Create your views here.
def userreview(request):
    ss=request.session['u_id']
    if request.method=="POST":
        obj=Review()
        obj.rating=request.POST.get('rtng')
        obj.text=request.POST.get('txt')
        obj.user_id = ss
        obj.save()
    return render(request,'review/User_review.html')

def merchntvewrevw(request):
    obj=Review.objects.all()
    context={
        'g':obj
    }
    return render(request,'review/Merchant_view_review.html',context)

def usrvewrvw(request):
    obj=Review.objects.all()
    context={
        'h':obj
    }
    return render(request,'review/User_view_review.html',context)