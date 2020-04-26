from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('home', views.home, name='home'),
    path('test',views.test, name = 'test'),
    path('stt',views.stt, name = 'stt'),
    path("editor",views.editor, name = "editor")
]