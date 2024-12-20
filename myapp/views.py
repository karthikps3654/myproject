from django.shortcuts import render
from .models import *
def index(request):
    students = student.objects.all()
    games = game.objects.all()

    return render(request,'index.html',{'students':students,'games':games})