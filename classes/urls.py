from django.urls import path
from .import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    #path('', views.index,name='index'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('', views.home,name='home'), 
    path('register/', views.registerpage,name='register'),  
    path('login/', views.loginpage,name='login'),  
    path('logout/', views.logoutUser,name='logout'), 
    path('update_order/<str:pk>/', views.updateteacher, name="update_teacher"),
    path('update_testinomial/<str:pk>/', views.updatetestinomial, name="update_testinomial"),
    path('updateresultslider/<str:pk>/', views.updateresultslider, name="updateresultslider"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),
]