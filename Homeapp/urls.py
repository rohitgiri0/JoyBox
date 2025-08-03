from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='loginpage'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('listing_form/',views.create_listing,name='create_listing'),
    path('listings/', views.browse_consoles, name='browse_consoles'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:pk>/', views.edit_listing, name='edit_listing'),
    path('delete/<int:pk>/', views.delete_listing, name='delete_listing'),
    path('listing/<int:pk>/', views.console_detail, name='console_detail'),
    path('chat/<str:username>/', views.chat_with_user, name='chat_with_user'),
    path('my-chats/', views.chat_list, name='chat_list'),
]