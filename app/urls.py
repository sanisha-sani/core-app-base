from django.urls import re_path
from .import views


urlpatterns = [
    
    re_path(r'^$', views.index, name='index'),
    re_path(r'^reportedissue$', views.reportedissue, name='reportedissue'),

#  --- Sanisha : Trainers and Trainees section ---

    re_path(r'^reportissuetrainers$', views.reportissuetrainers, name='reportissuetrainers'),
    re_path(r'^reportissuetrainees$', views.reportissuetrainees, name='reportissuetrainees'),
    re_path(r'^trainerunsolvedissue$', views.trainerunsolvedissue, name='trainerunsolvedissue'),
    re_path(r'^trainersolvedissue$', views.trainersolvedissue, name='trainersolvedissue'),
    re_path(r'^traineesunsolved$', views.traineesunsolved, name='traineesunsolved'),
    re_path(r'^traineessolved$', views.traineessolved, name='traineessolved'),

# --- Trainers and Trainees section end ---


# --- Jishnu : Report and Reported Issue section ---

    re_path(r'^reportissue$', views.reportissue, name='reportissue'),
    re_path(r'^reportedissuesub$', views.reportedissuesub, name='reportedissuesub'),

# --- Report and Reported Issue section end ---

]
