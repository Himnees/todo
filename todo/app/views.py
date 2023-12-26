from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form, 'tasks':tasks}
    return render(request, 'app/index.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form':form}
    return render(request, 'app/update.html', context)


def delete(request, pk):
    item= Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item':item}
    return render(request, 'app/delete.html', context)

