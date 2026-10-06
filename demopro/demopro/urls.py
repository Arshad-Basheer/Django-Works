"""
URL configuration for demopro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views import View

from myapp import views
from myapp.views import StudentFullUpdate

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.Goodmorning.as_view()),
    path('hw',views.Helloworld.as_view()),
    path('ge',views.Goodevening.as_view()),
    path('ud',views.UserDetails.as_view()),
    path('sd',views.StudentDetails.as_view()),
    path('sc',views.StudentCreate.as_view()),
    path('sa/<int:i>',views.StudentDetail.as_view()),
    path('sdl/<int:i>',views.StudentDelete.as_view()),
    path('sfu/<int:i>',views.StudentFullUpdate.as_view()),
    path('spu/<int:i>',views.StudentPartialUpdate.as_view()),

]
