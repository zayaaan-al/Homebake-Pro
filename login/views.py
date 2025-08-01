from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        passw = request.POST.get('password')
        obj = Login.objects.filter(user_name=username, password=passw)
        typ = ""
        for var in obj:
            typ = var.type
            uid = var.u_id
            if typ == "user":
                request.session['u_id'] = uid
                return HttpResponseRedirect('/temp/user/')
            elif typ == "admin":
                request.session['u_id'] = uid
                return HttpResponseRedirect('/temp/admin/')
            elif typ == "merchant":
                request.session['u_id'] = uid
                return HttpResponseRedirect('/temp/merchant/')
            else:
                objlist = "Incorrect email or password.. try again!!!..."
                context = {
                    'msg': objlist,
                }
            return render(request, 'login/login.html', context)
    return render(request,'login/login.html')
