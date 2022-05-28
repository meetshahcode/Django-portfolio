from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<p>Hello</p>")

def meet(request):
    return render(request,"workshtmlfiles/hello.html")
