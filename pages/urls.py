from . import views
from django.urls import path

urlpatterns = [
    path('', views.SessionList.as_view(), name='home'),
    path('<slug:slug>', views.SessionDetail.as_view(), name='session_detail')
]
