from os import name

from django.db.models import Model
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import HttpResponse,JsonResponse
from pip._internal.utils import retry

from myapp.models import Student

# Create your views here.
class Goodmorning(View):
    def get(self,request):
        data={"message":"Good Morning"}
        return JsonResponse(data)

class Helloworld(View):
    def get(self,request):
        data={"message":"Hello World"}
        return JsonResponse(data)

class Goodevening(View):
    def get(self,request):
        data={"message":"Good Evening"}
        return JsonResponse(data)

class UserDetails(View):
    def get(self,request):
        data = [

            {"name": "Arun", "age": 23, "place": "ekm"},
            {"name": "Amal", "age": 24, "place": "ekm"},
            {"name": "Anu", "age": 23, "place": "ekm"}
        ]

        return JsonResponse(data,safe=False)

class StudentDetails(View):
    def get(self,request):
        data=Student.objects.all().values()
        s=list(data)

        return JsonResponse(s,safe=False)

from json import loads

@method_decorator(csrf_exempt,name='dispatch')
class StudentCreate(View):
    def post(self,request):
        data = loads(request.body)

        r=data['rollnumber']
        n=data['name']
        a=data['age']
        p=data['place']
        m=data['marks']

        s=Student.objects.create(rollnumber=r,name=n,age=a,place=p,marks=m)
        s.save()

        return JsonResponse({"message":"Inserted data Succesfully"})


# Api view for reading a specific record
class StudentDetail(View):
    def get(self,request,i):
        s=list(Student.objects.filter(id=i).values())
        if s:
            return JsonResponse(s,safe=False)
        else:
            return JsonResponse({"message":"No student data"})

@method_decorator(csrf_exempt,name='dispatch')
class StudentDelete(View):
    def delete(self,request,i):
        s=Student.objects.get(id=i)
        s.delete()

        return JsonResponse({"Message":"Deleted Successfully"})

@method_decorator(csrf_exempt,name='dispatch')
class StudentFullUpdate(View):
    def put(self,request,i):
        data=loads(request.body)
        try:
            s=Student.objects.get(id=i)
            s.rollnumber=data['rollnumber']
            s.name=data['name']
            s.age=data['age']
            s.place=data['place']
            s.marks=data['marks']
            s.save()

            return JsonResponse({"message":"Successfully Updated"})

        except:
            return JsonResponse({"message":"No Student Data"})

@method_decorator(csrf_exempt,name='dispatch')
class StudentPartialUpdate(View):
    def patch(self,request,i):
        data=loads(request.body)

        try:
            s=Student.objects.get(id=i)

            if 'rollnumber' in data:
                s.rollnumber = data['rollnumber']
            if 'name' in data:
                s.name = data['name']
            if 'age' in data:
                s.age = data['age']
            if 'place' in data:
                s.place = data['place']
            if 'marks' in data:
                s.marks = data['marks']

            s.save()

            return JsonResponse({"message": "Successfully Updated"})

        except:
            return JsonResponse({"message": "No Student Data"})
