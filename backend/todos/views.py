"""
 todos/views.py
 -------------------------------------------------------------------------
 This file defines the business logic of how our Todos
 app responds to user requests.
"""

from rest_framework import generics

from . import models
from . import serializers


class ListTodo(generics.ListCreateAPIView):
    """
     A class defining how the Todo records will be returned to the general
     list AP call.
    """
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    """
     A class defining the ways our API will interact with a specific
     Todo record.
    """
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
