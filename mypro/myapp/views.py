from django.db.models import Model
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from myapp.models import Person
from myapp.models import Movie
# Create your views here.
# def first(request):
#     return HttpResponse("First Page")
#
# def second(request):
#     return HttpResponse("Second Page")
# class First(View):
#     def get(self,request):
#         return HttpResponse("""
#         <h1>First Page</h1>
#         <h1>Hello</h1>
#         """)

# class Second(View):
#     def get(self,request):
#         return HttpResponse("<h1>Second Page</h1>")

class First(View):
    def get(self,request):
        # data = [{'Name': 'Anandhan', 'Age': 22},{'Name': 'Abin', 'Age': 22},{'Name': 'Aravind', 'Age': 22}]
        data=Person.objects.all()
        context={'data':data}
        return render(request,'first.html',context)


class Second(View):
    def get(self,request):
        data = {'Company':'Google','Place':'Kochi'}
        return render(request,'second.html',context=data)

class Movie_list(View):
    def get(self,request):
        data=Movie.objects.all()
        context = {'data': data}
        return render(request, 'movie.html', context)

class Add_Movie(View):
    def get(self,request):
        return render(request,'addmovie.html')

    def post(self,request):
        # print(request.POST)
        data=request.POST
        n=data['name']
        d=data['director']
        y=data['year']
        print(n,d,y)

        #query for creating a new record in ORM
        #modelname.objects.create(column=value,column=value,column=value)
        m=Movie.objects.create(movie_name=n,director=d,year=y)
        m.save()
        return render(request,'addmovie.html')


