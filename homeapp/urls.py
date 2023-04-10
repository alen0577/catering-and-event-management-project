from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('usercreate/',views.usercreate,name='usercreate'),
    path('login/',views.login,name='login'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logout/',views.logout,name='logout'),

    

    path('user-home_page/',views.userhome,name='userhome'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.editpage,name='editpage'),
    path('edit_details/<int:pk>',views.editdetails,name='editdetails'),
    path('cart_page/',views.cart,name='cart'),
    path('delete_item/<int:pk>',views.deleteitem,name='deleteitem'),
    path('addcart/<int:pk>',views.add_to_cart,name='add_to_cart'),
    path('checkout/',views.checkout,name='checkout'),


    path('admin-home_page/', views.adminhome,name='adminhome'),
    path('category_page/',views.category,name='category'),
    path('add_category/',views.addcategory,name='addcategory'),
    path('product_page/',views.product,name='product'),
    path('add_product/',views.addproduct,name='addproduct'),
]