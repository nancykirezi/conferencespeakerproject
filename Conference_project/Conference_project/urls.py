"""
URL configuration for Conference_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.db import models
from conference import views as conference_views
from speakers import views as speaker_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('conferences/', conference_views.ConferenceListView.as_view(), name='conference_list'),
    path('conferences/create/', conference_views.ConferenceCreateView.as_view(), name='conference_create'),
    path('conferences/<int:id>/', conference_views.ConferenceDetailView.as_view(), name='conference_detail'),
    path('conferences/<int:id>/edit/', conference_views.ConferenceUpdateView.as_view(), name='conference_update'),
    path('conferences/<int:id>/delete/', conference_views.ConferenceDeleteView.as_view(), name='conference_delete'),

]
# Create your models here.
