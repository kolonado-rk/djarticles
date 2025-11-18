import json
from django.shortcuts import render
from rest_framework import viewsets

from articles.models import NewSource, Article, Digest, DigestArticle
from articles.serializers import NewSourceSerializer, ArticleSerializer, DigestSerializer, DigestArticleSerializer


class NewSourceView(viewsets.ModelViewSet):
    queryset = NewSource.objects.all()
    serializer_class = NewSourceSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class DigestView(viewsets.ModelViewSet):
    queryset = Digest.objects.all()
    serializer_class = DigestSerializer


class DigestArticleView(viewsets.ModelViewSet):
    queryset = DigestArticle.objects.all()
    serializer_class = DigestArticleSerializer
