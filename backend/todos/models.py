"""
 todos/models.py
 ------------------------------------------------------------------------------
 This file defines the database models for our Todo app.
"""

from django.db import models

class Todo(models.Model):
    "A simple model defining our todo tasks"
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=200, null=True)
    description=models.TextField(null=True)
    PRIORITY_CHOICES = (
      ('h', 'High Priority'),
      ('m', 'Medium Priority'),
      ('l', 'Low Priority')
    )
    priority=models.CharField(max_length=1, choices = PRIORITY_CHOICES, null=True)

    def __str__(self):
      """
       A string representation of this model.
      """
      return self.title
