
from django.urls import path,include
from account.views import UserRegistrationView,UserLoginView,UserProfileView,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView
from account import views

urlpatterns = [
    path("register/",UserRegistrationView.as_view(),name='register'),
    path("login/",UserLoginView.as_view(),name='login'),
    path("profile/",UserProfileView.as_view(),name='profile'),
    path("changepassword/",UserChangePasswordView.as_view(),name='changepassword'),
    path("reset/",SendPasswordResetEmailView.as_view(),name='reset'),
    path("reset-password/<uid>/<token>",UserPasswordResetView.as_view(),name='reset-password'),
    path('', views.index, name='home'),

]