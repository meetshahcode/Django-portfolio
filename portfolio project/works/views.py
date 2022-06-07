from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import work

def Homepage(request):
    works = work.objects
    return render(request,'workshtmlfiles/homepage.html',{'works':works})

def detail(request,Work_id):
    work_obj = get_object_or_404(work,pk = Work_id)
    return render(request,'workshtmlfiles/Detail.html',{'work':work_obj})
