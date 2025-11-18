from django.urls import path, include
from rest_framework.routers import DefaultRouter
from articles.views import NewSourceView, ArticleView, DigestView, DigestArticleView

router = DefaultRouter()
router.register(r'newsource', NewSourceView, basename='newsource')
router.register(r'article', ArticleView, basename='article')
router.register(r'digest', DigestView, basename='digest')
router.register(r'digestarticle', DigestArticleView, basename='digestarticle')

urlpatterns = [
    path('', include(router.urls)),
]
