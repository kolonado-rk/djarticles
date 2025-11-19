from datetime import timezone

from django.db import models

# Create your models here.
class NewSource(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    rss_url = models.CharField(max_length=200)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.ForeignKey(NewSource, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=200, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Digest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class DigestArticle(models.Model):
    id = models.AutoField(primary_key=True)
    digest = models.ForeignKey(Digest, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
