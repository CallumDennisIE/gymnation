from . import views
from django.urls import path

urlpatterns = [
    path('', views.SessionList.as_view(), name='home')
]
