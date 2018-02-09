"""
 todos/urls.py
 --------------------------------------------------------------
This file defines the url routing used by the
todos app.
"""

from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.ListTodo.as_view(), name='index'),
    path('<int:pk>/', views.DetailTodo.as_view(), name='detail'),
]
