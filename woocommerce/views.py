from django.shortcuts import render

def home_views(request):
    return render(request, "pages/home.html")


def contact_views(request):
    return render(request, "pages/contact.html")


def about_views(request):
    return render(request, "pages/about.html")


def cart_views(request):
    return render(request, "pages/cart-grocery.html")


def checkout_views(request):
    return render(request, "pages/checkout-grocery.html")


def grocery_details_views(request):
    return render(request, "pages/grocery-details.html")


def wishlist_views(request):
    return render(request, "pages/wishlist-grocery.html")


def grocery_product_views(request):
    return render(request, "pages/grocery-product.html")


def store_views(request):
    return render(request, "pages/store.html")


def blogDetails_views(request):
    return render(request, "pages/blog-details.html")


def blog_views(request):
    return render(request, "pages/blog.html")


def blogGrid_views(request):
    return render(request, "pages/blog-grid.html")


def portfolio_views(request):
    return render(request, "pages/portfolio.html")


def portfolioDetails_views(request):
    return render(request, "pages/portfolio-details.html")
