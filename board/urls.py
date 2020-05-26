from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from board import views

urlpatterns = [
    path('', views.homefunc, name='home'),
]