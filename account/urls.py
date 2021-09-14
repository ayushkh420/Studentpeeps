from django.urls import path, include
from django_email_verification import urls as email_urls
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import VerificationView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register', views.register, name='register'),
    path('yourdetail', views.yourdetail, name='yourdetail'),
    path('signup', views.signup, name='signup'),
    path('upload', views.upload, name='upload'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('YourDetail', views.YourDetail, name='YourDetail'),
    path('email/', include(email_urls)),
    # path('send_email', views.sendEmail, name="send_email"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),
    path('myaccount', views.myaccount, name="myaccount"),    
    path('636756-secret-upload-email-page', views.uploademail, name="Secret Page"),

    # Reset Password Urls
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
    name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
    name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
    name="password_reset_complete"),

] 