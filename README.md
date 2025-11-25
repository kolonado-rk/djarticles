# Project djarticles
###
### Adresar v Projecty pre novy project djarticles 
```shell script
$ sudo apt install python3.12
$ cd ~/Prjekty/django-app
$ mkdir djarticles        #vytvori projekt pre artikle
$ cd djarticles
$ python3.12 -m venv venv  #
```
### Instalacia potrebnych balikov pre django + postgresql
```shell script
$ pip install django
$ pip install psycopg2-binary
$ pip install djangorestframework

$ django-admin startproject djarticles .
$ python manage.py startapp articles
```

### Postgres 16 
- vytvorenie databazy articles
- vytvorenie uzivatela art_user
- pridelenie prav
```shell script
# CREATE DATABASE articles;
# CREATE USER art_user with password 'article_user';
# GRANT CONNECT, TEMPORARY ON DATABASE articles TO art_user;
# \c articles
# GRANT USAGE, CREATE ON SCHEMA public TO art_user;
# GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO art_user;
```
- migracia struktur z modelov do db articles
```shell script
$ python manage.py makemigration
$ python manage.py migrate 
```

### Vystavba aplikacie - casti:
#### 1.Models 
- from django.db import models
- tvorba class NewSource(models.Model)

#### 2.Serializers
- from rest_framework import serializers
- from articles.models import NewSource, Article, Digest, DigestArticle
- class NewSourceSerializer(serializers.ModelSerializer)

#### 3.Views
- from rest_framework import viewsets
- class NewSourceView(viewsets.ModelViewSet)
- nezabudnut pridat def index(request):
    return HttpResponse("Articles API beží 🙂")

#### 4.Routers
- from rest_framework.routers import DefaultRouter
- router.register(r'newsource', NewSourceView, basename='newsource')

#### 5.Users na prihlasenie do aplikacie
```shell script
$ python manage.py createsuperuser
$ Username (leave blank to use 'kolonado'): admin
$ Email address:      
$ Password: AdminUser2025*
$ Password (again): 
```
#### 6.Spustenie apky
- cez bash: python manage.py runserver
- cez pycharm chrobak!
- v prehliadaci: 127.0.0.1:8000/admin alebo  127.0.0.1:8000/api

#### 7. RSS feedy
- bash: pip install feedparser
- do djarticle dorobeny dir: management - commands - fetchrss.py
- python manage.py fetchrss
- ten automaticky naplni article z rss_url feedov