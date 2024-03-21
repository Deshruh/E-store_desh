from django.db import models
from users.models import User


class ArticleCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class ArticleTag(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256)
    annotation = models.CharField(max_length=256)
    article_text = models.TextField()
    images = models.ImageField(upload_to="article_images")
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to=ArticleCategory, on_delete=models.CASCADE)
    tags = models.ForeignKey(to=ArticleTag, on_delete=models.CASCADE)

    def __str__(self):
        return f"Статья: {self.name} | Аннотация: {self.annotation}"
