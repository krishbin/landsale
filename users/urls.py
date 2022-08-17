from django.urls import path
from django.contrib.auth import views as a_views
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='users-register'),
    path('profile/', views.userProfile, name='users-profile'),
    path('wishlist/', views.wishlist, name='users-wishlist'),
    path('to_wishlist/<int:id>/', views.addToWishlist, name='users-to-wishlist'),
    path('login/', a_views.LoginView.as_view(template_name='login.html'),name='users-login'),
    path('logout/', a_views.LogoutView.as_view(template_name='logout.html'),name='users-logout'),
    path('password-reset/', a_views.PasswordResetView.as_view(template_name='password-reset.html'),name='password_reset'),
    path('password-reset/done/', a_views.PasswordResetDoneView.as_view(template_name='password-reset-done.html'),name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', a_views.PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html'),name='password_reset_confirm'),
    path('password-reset/complete/', a_views.PasswordResetDoneView.as_view(template_name='password-reset-completed.html'),name='password_reset_complete'),
]
