from typing import List
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Items
# Create your views here.

def index(request):
    acts = Items.objects.all()
    if request.method == "POST":
        if request.POST['activity'] != "":
            instance = Items(task = request.POST['activity'])
            instance.save()
        else:
            pass
    return render (request, 'listtodo/index.html',{'holds': acts})


def delete(request, pk):
    acts = Items.objects.get(id=pk)
    acts.delete()
    return redirect('/')
    