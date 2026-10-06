from idlelib.rpc import request_queue

from django.shortcuts import render
from django.views import View
import math
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Add(View):
    def get(self,request):
        return render(request,'add.html')

    def post(self,request):
        data=request.POST
        a=data['a']
        b=data['b']
        res=int(a)+int(b)
        print(res)
        context={'result':res}
        return render(request,'add.html',context)

class Fact(View):
    def get(self,request):
        return render(request, 'fact.html')

    def post(self,request):
        data=request.POST
        n=data['n']
        f=math.factorial(int(n))
        context={'fact':f}
        return render(request,'fact.html',context)

class Bmi(View):
    def get(self,request):
        return render(request,'bmi.html')

    def post(self,request):
        data=request.POST
        w=data['w']
        h=data['h']
        hm=int(h)/100
        bmi=int(w)/(hm**2)
        context={'bmi':bmi}
        return render(request,'bmi.html',context)
