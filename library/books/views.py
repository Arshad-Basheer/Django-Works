from django.shortcuts import render
from django.templatetags.i18n import language
from django.views import View
from books.models import Book

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Add_Book(View):
    def get(self, request):
        return render(request, 'addbook.html')

    def post(self, request):
        data = request.POST
        t = data['t']
        a = data['a']
        p = data['p']
        l = data['l']
        n = data['n']
        m = Book.objects.create(title=t, author=a, price=p, language=l, pages=n)
        m.save()
        return render(request, 'addbook.html')

class View_books(View):
    def get(self,request):
        data=Book.objects.all()
        context = {'data': data}
        return render(request,'viewbook.html',context)