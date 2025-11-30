from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse  # môže tam zostať, ak ho používaš inde


from articles.models import NewSource, Article, Digest, DigestArticle
from articles.serializers import NewSourceSerializer, ArticleSerializer, DigestSerializer, DigestArticleSerializer


@login_required
def index(request):
    return render(request, "index.html")

class NewSourceView(viewsets.ModelViewSet):
    queryset = NewSource.objects.all()
    serializer_class = NewSourceSerializer
    permission_classes = [IsAuthenticated]


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


class DigestView(viewsets.ModelViewSet):
    queryset = Digest.objects.all()
    serializer_class = DigestSerializer
    permission_classes = [IsAuthenticated]


class DigestArticleView(viewsets.ModelViewSet):
    queryset = DigestArticle.objects.all()
    serializer_class = DigestArticleSerializer
    permission_classes = [IsAuthenticated]
