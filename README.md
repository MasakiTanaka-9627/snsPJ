# django-3.0.3

## 実行環境

* macOS Catalina version 10.15.3
* Docker version 19.03.5

## 作成環境

* Django==3.0.3
* python:3.8.2
* mysql:5.7

## ファイル構成

```
.
├── docker-compose.yml
├── Dockerfile 
├── Gemfile
└── Gemfile.lock

```

## 環境構築のやり方

```
1. docker-compose run --rm web django-admin startproject config .

config は任意に決めれるプロジェクト

2. config/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db', # MYSQL_DATABASE
        'USER': 'user', # MYSQL_USER
        'PASSWORD': 'password', # MYSQL_PASSWORD
        'HOST': 'db',
        'PORT': '3306',
    }
}


3. docker-compose up
