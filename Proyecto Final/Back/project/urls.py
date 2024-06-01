"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from project.views import cliente_view
from project.views import servicio_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/servicio', servicio_view.ServicioAPIView.as_view()),
    path('v1/servicio/<int:pk>/', servicio_view.ServicioDetailAPIView.as_view()),
    path('v2/cliente', cliente_view.ClienteAPIView.as_view()),
    path('v2/cliente/<int:pk>/', cliente_view.ClienteDetailAPIView.as_view()),
]
