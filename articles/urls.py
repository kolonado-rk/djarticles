from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import NewSourceView, ArticleView, DigestView, DigestArticleView
from .views import admin_article_filter_view  # <- pridaj import

router = DefaultRouter()
router.register(r'newsource', NewSourceView, basename='newsource')
router.register(r'article', ArticleView, basename='article')
router.register(r'digest', DigestView, basename='digest')
router.register(r'digestarticle', DigestArticleView, basename='digestarticle')


urlpatterns = [
    # iba appkové veci, žiadny admin tu:
    path("", views.index, name="articles_index"),  # GET / -> index
    path("api/", include(router.urls)),            # /api/... -> DRF viewsety
]
