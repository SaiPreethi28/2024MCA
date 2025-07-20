from django.urls import path
##from . import views
##
##urlpatterns = [
##    path('', views.product_list, name='product_list'),
##    path('product/<int:pk>/', views.product_detail, name='product_detail'),
##]



##from django.contrib.auth import views as auth_views
##from . import views
##
##urlpatterns = [
##    path('', views.product_list, name='product_list'),
##    path('product/<int:pk>/', views.product_detail, name='product_detail'),
##    path('signup/', views.signup, name='signup'),
##    path('login/', auth_views.LoginView.as_view(template_name='catalog/login.html'), name='login'),
##    path('logout/', auth_views.LogoutView.as_view(next_page='product_list'), name='logout'),
##]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('order/place/', views.place_order, name='place_order'),
    path('orders/', views.order_history, name='order_history'),
]

urlpatterns += [
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
]


urlpatterns += [
    path('place-order/', views.place_order, name='place_order'),
    path('order-history/', views.order_history, name='order_history'),
]



