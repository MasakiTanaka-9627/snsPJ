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
1. docker-compose run --rm web django-admin startproject config(プロジェクト名) .

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

環境構築はここで終了

---

4. docker-compose run --rm web　python manage.py startapp polls(アプリ名)

(コンテンツにattachしてほうが楽...)

5. INSTALLED_APPSにアプリ名を追加、'bootstrap4'も追加しておく

6. settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],　←追加
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins':[ 
                'bootstrap4.templatetags.bootstrap4',
            ],        
        },
    },
]

```
