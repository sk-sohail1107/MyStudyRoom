from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<str:pk>", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>", views.DeleteRoom, name="delete-room"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutPage, name="logout"),
    path("register/", views.registerPage, name="register"),
    path("delete-message/<str:pk>", views.DeleteMessage, name = "delete-message"),
    path("profile/<str:pk>", views.userProfile, name = "profile"),
    path("update-profile", views.updateUser, name="update-profile"),
   
]