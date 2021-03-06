"""FileAudioToText URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from Converter import views

urlpatterns = [
    path('', views.redirect_view),
    path('api/upload-video', views.uploadVideo, name="upload-video"),
    path('api/remove-video', views.removeVideo, name="remove-video"),
    path('api/split-video', views.splitVideo, name="split-video"),
    path('api/video-to-audio', views.videoToAudio, name="video-to-audio"),
    path('api/audio-to-text', views.audioToText, name="audio-to-text")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
