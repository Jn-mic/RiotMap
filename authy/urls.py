from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('post/', views.today_riot, name='post'),
    path('hotspot/', views.hotspot, name='hotspot'),
    path('profile/', views.profile, name='profile'),
    path('work/', views.work, name='work'),
    path('hospital/', views.hospital, name='hospital'),
    path('police/', views.police, name='police'),
]
    