from . import views

from django.urls import path

urlpatterns = [
    path('evalfaculty', views.evalfaculty, name='evalfaculty'),
    path('evallecturer', views.evallecturer, name='evallecturer'),


]