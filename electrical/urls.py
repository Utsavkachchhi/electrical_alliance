from django.urls import path
from . import views

urlpatterns = [
    path( '', views.index, name='index' ),
    path( 'restaurant/orderplaced/', views.orderplaced, name='orderplaced' ),
    path( 'distributors/', views.distributors, name='distributors' ),
    path( 'register/user/', views.customerRegister, name='register' ),
    path( 'login/user/', views.customerLogin, name='login' ),
    path( 'login/distributors/', views.distLogin, name='rlogin' ),
    path( 'register/distributors/', views.distRegister, name='rregister' ),
    path( 'profile/distributors/', views.distributorsProfile, name='rprofile' ),
    path( 'profile/user/', views.customerProfile, name='profile' ),
    path( 'user/create/', views.createCustomer, name='ccreate' ),
    path( 'user/update/<int:id>/', views.updateCustomer, name='cupdate' ),
    path( 'distributors/create/', views.createDistributors, name='rcreate' ),
    path( 'restaurant/update/<int:id>/', views.updateDistributors, name='rupdate' ),
    path( 'restaurant/orderlist/', views.orderlist, name='orderlist' ),
    path( 'distributors/menu/', views.menuManipulation, name='mmenu' ),
    path( 'logout/', views.Logout, name='logout' ),
    path( 'distributors/<int:pk>/', views.distributorsMenu, name='menu'),
    path( 'checkout/', views.checkout, name='checkout'),
    path('feedback/', views.Feedbackform, name='feedback'),
    path( 'about/', views.About, name='about' ),
    path( 'demo/', views.Demo, name='demo' ),
    path('delete/<int:id>',views.Return,name='delete'),
    # path( 'demolist/', views.Demo_list, name='demolist' ),

]