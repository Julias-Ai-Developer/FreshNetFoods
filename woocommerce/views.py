from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def home_views(request):
    return render(request, "pages/home.html")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect('dashboard')  # Redirect to user dashboard
            else:
                messages.error(request, "Incorrect password")
        except User.DoesNotExist:
            messages.error(request, "User with that email does not exist")

    return render(request, "pages/login.html")  # Render login page on GET or failed POST

# Make sure to protect the dashboard view
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # You can access user and client profile here via request.user and request.user.clientuser
    return render(request, "admin/dashboard.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = email.split('@')[0]  # or any logic to generate username
        password = request.POST.get("password")
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, "pages/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return render(request, "pages/register.html")

        if User.objects.filter(username=username).exists():
            username = username + str(User.objects.count() + 1)  # Ensure username is unique

        # Create user with hashed password
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        messages.success(request, "Registered successfully. Please login.")
        return redirect('login')  # or wherever you want to send the user

    return render(request, "pages/register.html")


def forgotpassword(request):
    return render(request, "pages/forgotpassword.html")


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


def blogDetails_views(request):
    return render(request, "pages/blog-details.html")


def blog_views(request):
    return render(request, "pages/blog.html")


def blogGrid_views(request):
    return render(request, "pages/blog-grid.html")


# admin dashboard Views
def dashboard(request):
    return render(request, "admin/dashboard.html")
