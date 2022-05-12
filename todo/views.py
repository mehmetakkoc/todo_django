from django.shortcuts import get_object_or_404, render, redirect
from .models import Todo
from .forms import TodoAppForm
from django.urls import path

# Create your views here.
def home(request):
    return render(request, 'todo/home.html')

def liste(request):
    todos = Todo.objects.all() 
    context = {
        'todos': todos,
    }
    return render(request, 'todo/liste.html', context)

def createTodo(request):
    form = TodoAppForm(request.POST or None)
    if form.is_valid():
        form.save()
        return (redirect('liste'))
    context = {'form': form}

    return render(request, 'todo/createTodo.html', context)
    
def updateTodo(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoAppForm(instance = todo)
    

    
    if request.method == 'POST':
        form = TodoAppForm(request.POST, instance= todo)
        form.save()
        return redirect('liste')
    context = {'form' : form}

    return render(request, 'todo/updateTodo.html', context )

def detailTodo(request, id):
    todoDetail = get_object_or_404(Todo, id = id)

    context = {'todoDetail': todoDetail}
    return render(request, 'todo/detailTodo.html', context)


def deleteTodo(request, id):
    todoDelete = get_object_or_404(Todo, id = id)
    if request.method == 'POST':
        todoDelete.delete()
        return redirect('liste')

    context = {'todoDelete': todoDelete}
    return render(request, 'todo/deleteTodo.html', context)
    