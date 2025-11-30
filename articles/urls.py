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
    path("admin/", admin.site.urls),

    # login/logout
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("admin/articles/filter/", admin_article_filter_view, name="admin_article_filter"),

    # tvoje stránky / API
    path("", views.index, name="articles_index"),  # GET / -> index
    path("api/", include(router.urls)),            # /api/... -> DRF viewsety
]
