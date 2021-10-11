from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('ai', views.ai, name='ai'),
    path('result', views.result, name='ai-result')
]
