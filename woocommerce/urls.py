from django.urls import path
from  .import views

urlpatterns = [

           path('' , views.home_views, name='home'),   
           path('login/' , views.login, name='login'), 
           path('register/' , views.register, name='register'), 
           path('forgotpassword/' , views.forgotpassword, name='forgotpassword'), 

           path('about/' , views.about_views, name='about'),   
           path('cart/' , views.cart_views, name='cart'),   
           path('wishlist/' , views.wishlist_views, name='wishlist'),   
           path('grocery-product/' , views.grocery_product_views, name='product'),   
           path('grocery-details/' , views.grocery_product_views, name='groceryDetails'),   
           path('checkout/' , views.checkout_views, name='checkout'),   
           path('blogDetails/' , views.blogDetails_views, name='blogDetails'),   
           path('blog/' , views.blog_views, name='blog'),   
           path('blogGrid/' , views.blogGrid_views, name='blogGrid'),  
           
           
           path('contact/' , views.contact_views, name='contact'),   

           #Admin Dashboard Paths
           path('dashboard/' , views.dashboard, name='dashboard'),

           
             
]