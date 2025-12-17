from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),  # ← article_list → post_list に変更
]
