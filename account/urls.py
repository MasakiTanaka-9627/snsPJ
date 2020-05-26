from django.urls import path
from .views import signupfunc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', signupfunc, name='signup'),
]