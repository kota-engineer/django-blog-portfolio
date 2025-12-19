# blog/admin.py
from django.contrib import admin
from .models import Post  # ← Article から Post に変更

admin.site.register(Post)

