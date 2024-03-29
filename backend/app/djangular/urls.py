"""djangular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import permissions
from django.conf.urls.static import static

urlpatterns = [
    path('docs', TemplateView.as_view(template_name="docs.html")),
    path('admin/', admin.site.urls),
    path('scrumboard/', include('scrumboard.urls')),
    path('auth_api/', include('auth_api.urls')),
    path('stocks/', include('stock.urls')),
    path('', ensure_csrf_cookie(TemplateView.as_view(template_name="stocks.html")))
] + static('static')
