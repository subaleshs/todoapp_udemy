from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def home(request):
    a = List.objects.all()
    return render(request,'todo\index1.html',{'jobs':a})