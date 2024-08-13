from django.shortcuts import render
from dinner.models import Menu
# Create your views here.

def func(request):
    result= Menu.objects.all()
    return render(request,'index.html',{'res':result})

def fun1(request):
    result=Menu.objects.all()
    if request.method=="POST":
        dish=request.POST.get("food")
        cost=request.POST.get("price")
        obj=Menu(item=dish,price=cost)
        obj.save()
        result=Menu.objects.all()
        return render(request,"food.html",{"res":result , "obj":obj})
    return render(request,"food.html")