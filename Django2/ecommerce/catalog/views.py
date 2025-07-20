##from django.shortcuts import render, get_object_or_404
##from .models import Product
##
##
##def product_list(request):
##    ob_products = Product.objects.all()
##    return render(request, 'product_list.html', {'products': ob_products})
##
##def product_detail(request, pk):
##    ob_product = get_object_or_404(Product, pk=pk)
##    return render(request, 'product_detail.html', {'product': ob_product})
##from django.shortcuts import render
##
### Create your views here.
##
##
##
##from .models import Product, Category
##
####def product_list(request):
####    category_id = request.GET.get('category')
####    if category_id:
####        products = Product.objects.filter(category_id=category_id)
####    else:
####        products = Product.objects.all()
####    categories = Category.objects.all()
####    return render(request, 'product_list.html', {'products': products, 'categories': categories})
##
##
##
##def product_list(request):
##    category_id = request.GET.get('category')
##    query = request.GET.get('q')
##    products = Product.objects.all()
##    if category_id:
##        products = products.filter(category_id=category_id)
##    if query:
##        products = products.filter(name__icontains=query)
##    categories = Category.objects.all()
##    return render(request, 'product_list.html', {'products': products, 'categories': categories})
##
##    return render(request, 'catalog/product_list.html', {'products': products, 'categories': categories})
##
##
##
##
##
##
##from django.contrib.auth.forms import UserCreationForm
##from django.shortcuts import redirect
##from django.contrib.auth import login
##
##def signup(request):
##    if request.method == 'POST':
##        form = UserCreationForm(request.POST)
##        if form.is_valid():
##            user = form.save()
##            login(request, user)
##            return redirect('product_list')
##          
##    else:
##        form = UserCreationForm()
##    return render(request, 'signup.html', {'form': form})
##
##
##
##def login(request):
##    if request.method == 'POST':
##        form = UserCreationForm(request.POST)
##        if form.is_valid():
##            user = form.save()
##            login(request, user)
##            return redirect('product_list')
##          
##    else:
##        form = UserCreationForm()
##    return render(request, 'login.html', {'form': form})
##
##
##
##
##
##def add_to_cart(request, pk):
##    cart = request.session.get('cart', [])
##    if pk not in cart:
##        cart.append(pk)
##    request.session['cart'] = cart
##    return redirect('product_list')
##
##def view_cart(request):
##    cart = request.session.get('cart', [])
##    products = Product.objects.filter(pk__in=cart)
##    return render(request, 'catalog/cart.html', {'products': products})
##
##
##
##
##from django.contrib.auth.decorators import login_required
##
##@login_required
##def place_order(request):
##    cart = request.session.get('cart', [])
##    if cart:
##        order = Order.objects.create(user=request.user)
##        order.products.set(cart)
##        order.save()
##        request.session['cart'] = []  # clear cart
##        return redirect('order_history')
##    return redirect('product_list')
##
##@login_required
##def order_history(request):
##    orders = Order.objects.filter(user=request.user)
##    return render(request, 'catalog/order_history.html', {'orders': orders})



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import Product, Category, Order  # Ensure Order is defined


# Product listing with optional filtering
def product_list(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')
    products = Product.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)
    if query:
        products = products.filter(name__icontains=query)

    categories = Category.objects.all()
    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories
    })


# Product detail view
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


# Signup view using Django's built-in UserCreationForm
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# ✅ FIXED: Correct login view using AuthenticationForm
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Add product to cart (via session)
def add_to_cart(request, pk):
    cart = request.session.get('cart', [])
    if pk not in cart:
        cart.append(pk)
    request.session['cart'] = cart
    return redirect('product_list')


# View cart contents
def view_cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(pk__in=cart)
    return render(request, 'cart.html', {'products': products})


# Place an order from the cart
@login_required
def place_order(request):
    cart = request.session.get('cart', [])
    if cart:
        order = Order.objects.create(user=request.user)
        order.products.set(cart)  # assumes ManyToManyField
        order.save()
        request.session['cart'] = []  # clear cart
        return redirect('order_history')
    return redirect('product_list')


# View user's order history
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'orders': orders})

