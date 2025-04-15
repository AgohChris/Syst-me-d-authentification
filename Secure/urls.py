from django.urls import path
from Secure import views


urlpatterns = [
    path("", views.home, name="home"),
    path("authentication", views.register, name="loginRegister"),
    path("register", views.register, name="register"),
    path("login", views.SignIn, name="login"),
    path("logout/", views.deconnection, name="logout"),
    path("activate", views.Activation_compte, name="activate"),
    

    path("mot-de-passe/oublié", views.demande_reset_mot_de_passe, name="demande_reset_password"),
    path("mot-de-passe/verification/<str:email>", views.verification_code_reset, name="verification_code_reset"),
    path("mot-de-passe/nouveau/<str:email>", views.Changement_de_mot_de_passe, name="changement_password"),
    
    # path("mot-de-passe/succes", views.reset_msg, name="reset_msg"),

]
