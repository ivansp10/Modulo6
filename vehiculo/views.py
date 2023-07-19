from django.shortcuts import render,HttpResponse


def index(request):
    return HttpResponse("<h1> bienvenidos</h1>")
# Create your views here.
