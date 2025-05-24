from django.contrib import admin
from django.urls import path
from  scripture_app.views import welcome_view, emotion_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_view, name='welcome_view'),
    path('emotions/', emotion_view, name='emotion_view'),
]