from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home, name="home"),
    path('login/', views.LoginUser, name="login"),
    path('register/', views.Register, name='register'),
    path('logout/', views.LogoutUser, name='logout'),
    path('<str:user_name>/upload_file', views.Upload, name='upload_file'),
    path('profile/<str:user_name>', views.Profile, name='profile'),
    path('delete/<int:post_id>', views.DeletePost, name='delete'),
    path('search/', views.Search, name='search'),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="main/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"), 
        name="password_reset_complete"),
]