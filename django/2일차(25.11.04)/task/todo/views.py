from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from todo.models import Todo

def todo_list(request):
    todos = Todo.objects.all().values_list("id", "title")
    result = [{'id': todo[0], 'title': todo[1]} for i, todo in enumerate(todos)]
    return render(request, "task.html", {'result': result})

def todo_detail(request, todo_id):
    try:
        todo = Todo.objects.get(id = todo_id)
        info = {
            'title': todo.title,
            'description': todo.description,
            'start_date': todo.start_date,
            'end_date': todo.end_date,
            'is_completed': todo.is_completed,
        }
        return render(request, "task_info.html", {"data":info})
    except Todo.DoesNotExist:
        raise Http404("Todo dose not found")

