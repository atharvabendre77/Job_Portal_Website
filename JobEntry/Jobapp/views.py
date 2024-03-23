from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import *
from .models import Job
from django.db.models import Q

# Create your views here.

def index(request):
    context={}
    uid=request.user.id
    j=Job.objects.all
    context['job']=j
    # print(p)
    # print("login user id",uid)
    return render(request,'index.html',context)
    

# def jobdetail(request):
#     return render(request,"jobdetail.html")
def jobdetail(request,jid):
    j=Job.objects.filter(id=jid)
    context={}
    context['job']=j
    # uid=request.user.id
    return render(request, "jobdetail.html",context)



def joblist(request):
    return render(request,"joblist.html")

def contact(request):
    return render(request,"contact.html")

def category(request):
    return render(request,"category.html")

def about(request):
    return render(request,"about.html")

def testimonial(request):
    return render(request,"testimonial.html")

def error(request):
    return render(request,"error.html")

def base(request):
    return render(request, "base.html")

def user_login(request):
    context = {}
    if request.method == "POST":
        usr = request.POST["uname"]
        pwd = request.POST["pass"]
        if usr == "" or pwd == "":
            context["errmsg"] = "Field cannot be empty"
            return render(request, "login.html", context)
        else:
            u = authenticate(username=usr, password=pwd)
            if u is not None:
                login(request, u)
                return redirect("/")
            else:
                context["errmsg"] = "Invalid username and password"
                return render(request, "login.html", context)
    else:
        return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("/login")


def register(request):
    context = {}
    if request.method == "POST":
        uname = request.POST["uname"]
        upassword = request.POST["upass"]
        ucpassword = request.POST["ucom"]
        if uname == "" or upassword == "" or ucpassword == "":
            context["errmsg"] = "Field can not be Empty!!!"
            return render(request, "register.html", context)

        elif upassword != ucpassword:
            context["errmsg"] = "INVALID PASSWORD...TRY AGAIN"
            return render(request, "register.html", context)

        else:
            try:
                u = User.objects.create(username=uname, email=uname, password=upassword)
                u.set_password(upassword)
                u.save()
                context["success"] = "registration successfully"
                return render(request, "register.html", context)
            except Exception:
                context["errmsg"] = "Username Already Exists"
                return render(request, "register.html", context)

    else:
        return render(request, "register.html", context)
    

def catfilter(request,cv):
    q1=Q(cat=cv)
    q2=Q(is_active=True)

    
    u=Job.objects.filter(q1 & q2)
    context={}
    context['job']=u
    return render(request,'index.html',context)
    
    




