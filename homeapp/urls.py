from django.urls import path
from . import views

urlpatterns = [

#basic url paths 
#    
    path('',views.index,name='index'),
    path('usercreate/',views.usercreate,name='usercreate'),
    path('login/',views.login,name='login'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logout/',views.logout,name='logout'),

    
#user related url paths

    path('user-home_page/',views.userhome,name='userhome'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.editpage,name='editpage'),
    path('edit_details/<int:pk>',views.editdetails,name='editdetails'),
    path('cart_page/',views.cart,name='cart'),
    path('delete_item/<int:pk>',views.deleteitem,name='deleteitem'),
    path('addcart/<int:pk>',views.add_to_cart,name='add_to_cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('eventbooking/',views.eventbooking,name='eventbooking'),
    path('bookinglist/',views.bookinglist,name='bookinglist'),
    path('deleteevent/<int:pk>',views.deleteevent,name='deleteevent'),
    path('packages/',views.packages,name='packages'),
    


#admin related url paths

    path('admin-home_page/', views.adminhome,name='adminhome'),
    path('category_page/',views.category,name='category'),
    path('add_category/',views.addcategory,name='addcategory'),
    path('product_page/',views.product,name='product'),
    path('add_product/',views.addproduct,name='addproduct'),
    path('show_products/',views.showprdt,name='showprdt'),
    path('editproduct/<int:pk>',views.editproduct,name='editproduct'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete_product/<int:pk>',views.deleteprdt,name='deleteprdt'),
    path('show_users/',views.showusr,name='showusr'),
    path('delete_user/<int:pk>',views.deleteusr,name='deleteusr'),
    path('addeventpacks/',views.addeventpacks,name='addeventpacks'),
    path('addmenupacks/',views.addmenupacks,name='addmenupacks'),
    path('eventrequest/',views.eventrequest,name='eventrequest'),
    path('approvedbookings/',views.approvedbookings,name='approvedbookings'),
    path('approve/<int:pk>',views.approve,name='approve'),
    path('reject/<int:pk>',views.reject,name='reject'),


]