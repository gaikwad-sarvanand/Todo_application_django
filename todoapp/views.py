from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoModel
from .forms import TodoForm
# Create your views here.


def index(request):
    return render(request, "index.html")


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("todo:add_todo")
    else:

        form = TodoForm()
        todos = TodoModel.objects.filter(is_done=False)
        return render(request, "add_todo.html", {'form': form, 'todos': todos})


def detail_todo(request, pk):
    todos = get_object_or_404(TodoModel, pk=pk)
    change_status = request.GET.get('change_status', '')
    if change_status:
        todos.is_done = True
        todos.save()
    return render(request, "detail.html", {'todos': todos})
