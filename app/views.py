from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def reportedissue(request):
    return render(request,'reportedissue.html')

#  --- Sanisha : Trainers and Trainees section ---

def reportissuetrainers(request):
    return render(request,'reportissuetrainers.html')

def reportissuetrainees(request):
    return render(request,'reportissuetrainees.html')

def trainerunsolvedissue(request):
    return render(request,'trainerunsolvedissue.html')

def trainersolvedissue(request):
    return render(request,'trainersolvedissue.html')

def traineessolved(request):
    return render(request,'traineessolved.html')

def traineesunsolved(request):
    return render(request,'traineesunsolved.html')

#  --- Trainers and Trainees section end ---

