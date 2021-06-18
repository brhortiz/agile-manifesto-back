"""agilemanifestobackend URL Configuration

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

from agilemanifesto import api

urlpatterns = [
    path('admin/', admin.site.urls),

    path('principles/', api.AgilePrincipleList.as_view()),
    path('principle/create/', api.CreateAgilePrinciple.as_view()),
    path('principle/<int:pk>/edit', api.UpdateAgilePrinciple.as_view()),
    path('principle/<int:pk>/delete', api.DeleteAgilePrinciple.as_view()),

    path('values/', api.AgileValueList.as_view()),
    path('value/create/', api.CreateAgileValue.as_view()),
    path('value/<int:pk>/edit', api.UpdateAgileValue.as_view()),
    path('value/<int:pk>/delete', api.DeleteAgileValue.as_view()),
]
