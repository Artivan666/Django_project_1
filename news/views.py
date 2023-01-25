from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('<h1>Main page</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')

def category(request, cat_id):
    if cat_id == 3:
        return redirect('home')
    return HttpResponse(f'<h1>Category</h1><p>{cat_id}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found =(</h1>')
