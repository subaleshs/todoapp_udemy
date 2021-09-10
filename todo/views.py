from django import forms
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views.decorators.http import require_POST


def home(request):
    a = List.objects.order_by('id')
    return render(request,'todo\index1.html',{'jobs':a,'form':jobInput})

@require_POST
def addTolist(request):
    frm = jobInput(request.POST)
    if frm.is_valid():
        val = request.POST['inp']
        newJob = List(job=val)
        print(val)
        newJob.save()
    return redirect('home')

def jobComplete(request,jobid):
    works = List.objects.get(pk=jobid)
    works.status = True
    works.save()
    return redirect('home')

def delCompleted(request):
    print('yo')
    List.objects.filter(status__exact = True).delete()
    return redirect('home')

def delAll(request):
    List.objects.all().delete()
    return redirect('home')