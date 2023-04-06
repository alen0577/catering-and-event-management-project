from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('admin-home_page/', views.adminhome,name='adminhome'),
    path('user-home_page/',views.userhome,name='userhome'),
]