from django.contrib import admin
from myapp.models import Person
from myapp.models import Movie
# Register your models here.

admin.site.register(Person)
admin.site.register(Movie)
