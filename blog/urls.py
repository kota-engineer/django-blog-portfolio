from django.contrib import admin
from django.urls import path
from blog import views  # blog アプリの views をインポート

urlpatterns = [
    # 管理サイト
    path('admin/', admin.site.urls),

    # 記事一覧ページ
    path('', views.post_list, name='post_list'),  # ルート URL に記事一覧を表示

    # カテゴリ一覧ページ
    path('category/', views.category_list, name='category_list'),  # カテゴリ一覧ページへの URL
]



