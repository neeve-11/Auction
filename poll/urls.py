from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'poll'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('register/', views.register_confirmation, name='register'),
    path('login/', views.login_page, name='login'),
    path('login_con/',views.login_confirmation, name='clogin'),
    path('inbox/', views.inbox, name='inbox'),
    path('logout/', views.logout_view, name='logout'),
    path('makebid/', views.create_bid, name='createbid'),
    path('bidconfirm/', views.bid_form, name='cbid'),
    path('mybid/', views.user_bid, name='mybid'),
    path('comment/', views.comment_bid, name='comment'),
    path('bidp/', views.price_bid, name='pbid'),
    path('listl/',views.listingl, name='listl'),
    path('list/', views.listing, name='list'),
    path('result/', views.result_bid, name='result'),
    path('about/', views.about, name='about'),
]
