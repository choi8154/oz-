"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path
from django.http import Http404
from django.shortcuts import render, redirect

movie_list = [
    {"title": "파묘", "director": "장재현"},
    {"title": "파묘1", "director": "장재현1"},
    {"title": "파묘2", "director": "장재현2"},
    {"title": "파묘3", "director": "장재현3"},
]
def index(request):
    return HttpResponse("Hello world")
def book_list(request):
    # book_text = ''
    # for i in range(0, 10):
    #     book_text += f'book {i}<br>'
    # return HttpResponse(book_text)
    return render(request, "book_list.html", {'range': range(0,10)})

def book(request, num):
    return render(request, "book_detail.html", {"num": num})

def language(request, lang):
    return HttpResponse(f"{lang}언어 페이지 입니다.")

def movies(request):
    # movie_title = [f"<a href='/movie/{index}'>{movie['title']}</a>" for index, movie in enumerate(movie_list)]
    # return HttpResponse("<br>".join(movie_title))
    return render(request, 'movies.html', {'movie_list': movie_list})

def movie_detail(request, num):
    if num > len(movie_list) - 1:
        raise Http404
    movie = movie_list[num]
    context = {"movie":movie}
    return render(request, 'movie.html', context)

def gugu(request, num):
    if num < 2:
        return redirect('/gugu/2')
    context = {
        "num": num,
        "result" : [num * i for i in range(1, 10)]
    }
    return render(request, "gugu.html", context=context)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('books/', book_list),
    path('books/<int:num>/', book),
    path('books/<str:lang>/', language),
    path('movie/', movies),
    path('movie/<int:num>/', movie_detail),
    path('gugu/<int:num>', gugu),

]
