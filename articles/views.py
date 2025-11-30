from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.http import HttpResponse  # môže tam zostať, ak ho používaš inde

from .forms import ArticleFilterForm
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


@staff_member_required
def admin_article_filter_view(request):
    """
    Vlastná admin stránka: admin si vyberie Article a my zobrazíme
    napr. DigestArticle záznamy, ktoré s ním súvisia + nejaký filter.
    """
    form = ArticleFilterForm(request.GET or None)

    # základný queryset – napr. všetky DigestArticle
    queryset = DigestArticle.objects.select_related("article").all()

    if form.is_valid():
        article = form.cleaned_data.get("article")
        only_published = form.cleaned_data.get("only_published")

        if article:
            queryset = queryset.filter(article=article)

        # TOTO si prispôsob podľa reálneho poľa v Article alebo DigestArticle
        if only_published:
            queryset = queryset.filter(article__is_published=True)
            # alebo queryset = queryset.filter(status="published")
            # podľa toho, čo máš v modeli

    context = {
        "form": form,
        "results": queryset,
    }
    return render(request, "admin_article_filter.html", context)
