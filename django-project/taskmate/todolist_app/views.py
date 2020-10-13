from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import Taskform
from django.contrib import messages
# Create your views here.
def todolist(request):
    if request.method == "POST":
        form=Taskform(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("task added!"))

        return redirect('/todolist/')
    else:
        all_tasks=TaskList.objects.all
        return render(request, 'todolist.html',{'all_tasks':all_tasks})

def delete_task(request, task_id):
    task=TaskList.objects.get(pk=task_id)
    task.delete()

    return redirect('todolist')

def complete_task(request, task_id):
    task=TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()

    return redirect('todolist')

def pending_task(request, task_id):
    task=TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')



def edit_task(request, task_id):
    if request.method=="POST":
        test=TaskList.objects.get(pk=task_id)
        form=Taskform(request.POST or None, instance=test)
        if form.is_valid():
            form.save()
        messages.success(request,("task edited"))
        return redirect ('todolist')
    else:
        task_obj=TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj':task_obj})


def contact(request):
    all_tasks=TaskList.objects.all
    return render(request, 'contact.html',{'all_tasks':all_tasks})


def about(request):
    all_tasks=TaskList.objects.all
    return render(request, 'about.html',{'all_tasks':all_tasks})
