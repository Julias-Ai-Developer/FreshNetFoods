from django.urls import path
from  .import views

urlpatterns = [

           path('' , views.home_views, name='home'),   
           path('about/' , views.about_views, name='about'),   
           path('cart/' , views.cart_views, name='cart'),   
           path('wishlist/' , views.wishlist_views, name='wishlist'),   
           path('grocery-product/' , views.grocery_product_views, name='product'),   
           path('grocery-details/' , views.grocery_product_views, name='groceryDetails'),   
           path('checkout/' , views.checkout_views, name='checkout'),   
           path('store/' , views.store_views, name='store'),   
           path('blogDetails/' , views.blogDetails_views, name='blogDetails'),   
           path('blog/' , views.blog_views, name='blog'),   
           path('blogGrid/' , views.blogGrid_views, name='blogGrid'),  
           
            path('portfolio/' , views.portfolio_views, name='portfolio'),   
           path('portfolioDetails/' , views.portfolioDetails_views, name='portfolioDetails'),  

           path('contact/' , views.contact_views, name='contact'),   
             
]