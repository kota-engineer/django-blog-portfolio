from django.db import models

class Category(models.Model):
    """
    記事カテゴリモデル
    - name: カテゴリ名
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    記事タグモデル
    - name: タグ名
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    ブログ記事モデル
    - title: 記事タイトル
    - body: 記事本文
    - created_at: 記事の作成日時（自動設定）
    - updated_at: 記事の最終更新日時（自動設定）
    - category: 記事のカテゴリ（外部キー）
    - tags: 記事のタグ（多対多）
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # カテゴリは1記事につき1つ
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    # タグは1記事につき複数
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
