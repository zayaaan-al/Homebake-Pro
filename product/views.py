from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from product.models import Product

# Create your views here.
def product(request):
    ss=request.session['u_id']
    if request.method=="POST":
        obj=Product()
        obj.product_name=request.POST.get("name")
        obj.image=request.POST.get("img")
        obj.price=request.POST.get("Price")
        obj.quantity=request.POST.get("qty")
        obj.offer=request.POST.get("offer")
        obj.ingredients=request.POST.get("ingrs")
        obj.quantity=request.POST.get('qty')
        # obj.image=request.POST.get('img')
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name
        obj.offer=request.POST.get('Offer')
        obj.merchant_id=ss
        obj.rating="1"
        obj.save()
    return render(request,'product/product.html')

def vewprdctandordr(request):
    obj=Product.objects.all()
    context={
        'w':obj
    }
    return render(request,'product/view_product_and_order.html',context)
