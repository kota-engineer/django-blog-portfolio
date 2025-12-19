"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/

Function views example:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views example:
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf example:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# accountsアプリのビューをインポート（プロフィール表示用）
from accounts.views import profile_view

urlpatterns = [
    # 管理サイト
    path('admin/', admin.site.urls),

    # ブログアプリのURLをinclude
    path('blog/', include('blog.urls')),

    # プロフィールページ: /profile/ でアクセス
    path('profile/', profile_view, name='profile'),
]
