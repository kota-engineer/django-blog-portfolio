from django.urls import path
from . import views  # 同じアプリ内の views.py からインポート

urlpatterns = [
    path('profile/', views.profile, name='profile'),  # プロフィールページ用 URL
]
