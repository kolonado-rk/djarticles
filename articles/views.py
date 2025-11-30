from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.decorators import login_required

from articles.models import NewSource, Article, Digest, DigestArticle
from articles.serializers import NewSourceSerializer, ArticleSerializer, DigestSerializer, DigestArticleSerializer
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from .forms import ArticleFilterForm
from .models import Article, DigestArticle


@staff_member_required
def admin_article_filter_view(request):
    form = ArticleFilterForm(request.GET or None)

    queryset = DigestArticle.objects.select_related("article").all()

    if form.is_valid():
        article = form.cleaned_data.get("article")
        only_recent = form.cleaned_data.get("only_recent")

        if article:
            queryset = queryset.filter(article=article)

        if only_recent:
            seven_days_ago = timezone.now() - timedelta(days=7)
            queryset = queryset.filter(article__published__gte=seven_days_ago)

    context = {
        "form": form,
        "results": queryset,
    }
    return render(request, "admin_article_filter.html", context)

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


@staff_member_required
def admin_article_filter_view(request):
    form = ArticleFilterForm(request.GET or None)

    queryset = DigestArticle.objects.select_related("article").all()

    if form.is_valid():
        article = form.cleaned_data.get("article")
        only_recent = form.cleaned_data.get("only_recent")

        if article:
            queryset = queryset.filter(article=article)

        if only_recent:
            seven_days_ago = timezone.now() - timedelta(days=7)
            queryset = queryset.filter(article__published__gte=seven_days_ago)

    context = {
        "form": form,
        "results": queryset,
    }
    return render(request, "admin_article_filter.html", context)
