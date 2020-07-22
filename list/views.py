from django.shortcuts import render, redirect
from django.http import HttpResponse
from list.forms import listform
from .models import listdb


def homepage(request):
    tasks = listdb.objects.all()
    form = listform()
    if request.method == 'POST':
        form = listform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'home.html', context)


def updatelist(request, pk):
    tasks = listdb.objects.get(id=pk)
    form = listform(instance=tasks)
    if request.method == "POST":
        form = listform(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'update.html', context)


def deletetask(request, pk):
    item = listdb.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'delete.html', context)
