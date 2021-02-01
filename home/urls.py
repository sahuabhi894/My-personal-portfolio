from django.urls import path
from . import views





urlpatterns = [
    
    path('',views.homepage,name='home'),
    path('contact', views.contact, name="contact"),

    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout/', views.handelLogout, name="handleLogout"),
]



