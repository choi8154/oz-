from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Todo
from todo.form import TodoForm

# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(complate=False)
    context = {
        "todos":todos
    }
    return render(request, "todo/todo_list.html", context)

def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    context = {
        "todo":todo,
    }
    return render(request, "todo/todo_detail.html", context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.save()
        return redirect("todo_list")
    context = {
        'form':form,
    }
    return render(request, 'todo/todo_post.html', context)

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.save()
        return redirect("todo_list")
    context = {
        'form':form,
    }
    return render(request, "todo/todo_post.html", context)

def done_list(request):
    dones = Todo.objects.filter(complate=True)
    context = {
        "dones":dones
    }
    return render(request, "todo/done_list.html", context)

def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complate = True
    todo.save()
    return redirect('todo_list')