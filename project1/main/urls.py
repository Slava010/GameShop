from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('SingIn', views.SingIn),
    path('SingUp', views.SingUp),
    path('Exit', views.Exit),
    path("Sort", views.Sort),
    path("Search", views.Search),
    path("Remove", views.Remove),
    path("about", views.About),
    path("Comment", views.Comment),

    path("AddGame", views.AddGame),
    path("Change", views.Change),
]