from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='loginpage'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('listing_form/',views.create_listing,name='create_listing'),
    path('listings/', views.browse_consoles, name='browse_consoles'),
]