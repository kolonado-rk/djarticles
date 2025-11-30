"""
URL configuration for djarticles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# djarticles/urls.py
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from articles.views import admin_article_filter_view  # <- import nášho view

urlpatterns = [
    path("admin/", admin.site.urls),

    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # DRF browsable API login
    path("api-auth/", include("rest_framework.urls")),

    # naša „admin“ stránka, ale mimo /admin/ prefixu:
    path("articles/filter/", admin_article_filter_view, name="admin_article_filter"),

    # appkové URL (index, /api/ atď.)
    path("", include("articles.urls")),
]
