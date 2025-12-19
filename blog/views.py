# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.db.models import Q  # OR検索用
from .models import Post, Category, Tag

def post_list(request):
    """
    記事一覧ページ + 検索・カテゴリ・タグ絞り込み対応
    """
    # --- GETパラメータを取得 ---
    query = request.GET.get('q')           # 検索キーワード
    category_id = request.GET.get('category')  # カテゴリID
    tag_id = request.GET.get('tag')           # タグID

    # --- 投稿データを取得 ---
    posts = Post.objects.all()

    # --- 検索キーワードによる絞り込み ---
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(body__icontains=query))

    # --- カテゴリによる絞り込み ---
    if category_id:
        posts = posts.filter(category__id=category_id)

    # --- タグによる絞り込み ---
    if tag_id:
        posts = posts.filter(tags__id=tag_id)

    # --- テンプレートに渡すデータ ---
    categories = Category.objects.all()  # フィルター用
    tags = Tag.objects.all()             # フィルター用

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags,
    })

def category_list(request):
    """
    カテゴリ一覧ページ
    """
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})


