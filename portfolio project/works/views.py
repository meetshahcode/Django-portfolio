from django.shortcuts import render
from django.http import HttpResponse
from .models import work

def Homepage(request):
    works = work.objects
    return render(request,'workshtmlfiles/homepage.html',{'works':works})
