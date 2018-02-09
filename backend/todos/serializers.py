"""
 todos/serializers.py
 -------------------------------------------------------------------------
 This file defines the data serializers used to transform
 the data sent from and to this back-end app.
"""

from rest_framework import serializers
from . import models


class TodoSerializer(serializers.ModelSerializer):
    """
     A serializer specific to the Todos model object.
    """
    class Meta:
        fields = (
            'id',
            'date_created',
            'date_modified',
            'title',
            'description',
            'priority',
        )
        model = models.Todo
