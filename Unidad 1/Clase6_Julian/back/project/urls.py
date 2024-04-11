"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from api.views.universidad_view import *
from api.views.post_view import *
from django.conf.urls import include
from api.views.universidad_view import UniversidadAPIView, UniversidadDetailAPIView
from api.views.post_view import PostAPIView, PostDetailAPIView

app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', PostAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('universidad/', UniversidadAPIView.as_view(), name='universidad-list'),
    path('universidad/<int:pk>/', UniversidadDetailAPIView.as_view(), name='universidad-detail'),
    
]
