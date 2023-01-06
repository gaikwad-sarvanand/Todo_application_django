from django.shortcuts import render, redirect
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
        todos = TodoModel.objects.all()
        return render(request, "add_todo.html", {'form': form, 'todos': todos})
