from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_about_page, name='about'),
    path('<slug:slug>', views.SessionDetail.as_view(), name='session_detail'),
    path('classes/', views.SessionList.as_view(), name='classes'),
    path('attend/<slug:slug>', views.SessionAttend.as_view(), name='session_attend'),
    path('our-team/', views.get_our_team_page, name='our_team'),
    path('shop/', views.get_shop_page, name='shop'),
    path('contact-us/', views.get_contact_us_page, name='contact_us')
]
