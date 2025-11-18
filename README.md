# Project djarticles
###
### Zalozit do adresara Projecty pre django novy project djarticles 
```shell script
$ sudo apt install python3.12
$ cd ~/Prjekty/django-app
$ mkdir djarticles        #vytvori projekt pre artikle
$ cd djarticles
$ python3.12 -m venv venv  #
```
### Doinstalovat potrebne baliky 
```shell script
$ pip install django
$ pip install psycopg2-binary

$ django-admin startproject djarticles .
$ python manage.py startapp articles
```

### Postgres 16 
- vytvorenie databazy articles
- vyvorenie uzivatela art_user
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

