"""
MASA Todo Cloud Engine: Task Orchestrator
Developer: MASA
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    all_todo_items = TodoItem.objects.all().order_by('-id')
    return render(request, 'todolist.html', {'all_items': all_todo_items})


def addTodo(request):
    content = request.POST.get('content', '').strip()
    if content:
        TodoItem.objects.create(content=content)
    return HttpResponseRedirect('/')


def deleteTodo(request, todo_id):
    try:
        item = TodoItem.objects.get(id=todo_id)
        item.delete()
    except TodoItem.DoesNotExist:
        pass
    return HttpResponseRedirect('/')
