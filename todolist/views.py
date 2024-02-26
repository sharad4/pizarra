from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Todolist

def add(request, project_id):
    return render(request, 'todolist/add.html')
