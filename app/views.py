from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def reportedissue(request):
    return render(request,'reportedissue.html')

def reportissuetrainers(request):
    return render(request,'reportissuetrainers.html')

def trainerunsolvedissue(request):
    return render(request,'trainerunsolvedissue.html')

def trainersolvedissue(request):
    return render(request,'trainersolvedissue.html')

def reportissuetrainees(request):
    return render(request,'reportissuetrainees.html')

def traineessolved(request):
    return render(request,'traineessolved.html')

def traineesunsolved(request):
    return render(request,'traineesunsolved.html')