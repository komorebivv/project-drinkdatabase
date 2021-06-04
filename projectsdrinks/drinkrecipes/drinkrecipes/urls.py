"""drinkrecipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('searchdrink.urls')),
    path('alcohol', include('searchdrink.urls')),
    path('otherdrink', include('searchdrink.urls')),
    path('fruit', include('searchdrink.urls')),
    path('otheradd', include('searchdrink.urls')),
    path('admin/', admin.site.urls),
]
