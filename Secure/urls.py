from django.urls import path
from Secure import views


urlpatterns = [
    path("", views.home, name="home"),
    path("authentication", views.register, name="loginRegister"),
    path("register", views.register, name="register"),
    path("login", views.SignIn, name="login"),
    path("logout/", views.deconnection, name="logout"),
    path("activate", views.Activation_compte, name="activate"),
    
    path("reset", views.demamde_reinital, name="reset"),
    path("resetpassword", views.resetpassword, name="reset"),
    path("emailenterforresetpassword", views.emailenter, name="emailenter"),
    path("sendmail", views.resetmsg, name="sendmail"),

]
