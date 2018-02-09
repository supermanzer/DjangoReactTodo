"""
 todos/admin.py
 -------------------------------------------
 This file defines how the database models are rendered in the admin page.
"""

from django.contrib import admin
from .models import Todo

admin.site.register(Todo)
