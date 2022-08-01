from django.urls import path
from . import views
from .views import Index , store
from .views import Signup, Login, logout
from .auth import  auth_middleware
from .views import Cart, CheckOut, OrderView, search


urlpatterns=[
	path('', Index.as_view(), name='homepage'),
	path('store', store , name='store'),
    path('search', search , name="search"),
	#path('search',SearchResultsView.as_view(), name="search"),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),


]