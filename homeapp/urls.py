from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logout/',views.logout,name='logout'),
    path('admin-home_page/', views.adminhome,name='adminhome'),
    path('user-home_page/',views.userhome,name='userhome'),
]