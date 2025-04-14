from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import random as rd
import uuid
from django.utils import timezone
from datetime import timedelta
# import ssl


# @login_required
def home(request):
    user = request.user
    return render(request, "home.html", {'user': user})



def register(request):
    
    if request.method == "POST":
        username=request.POST.get("username")
        email = request.POST.get("email").lower()
        password=request.POST.get("password")
        password1=request.POST.get("password1")
        
        if not (username and password and password1 and email):
            messages.error(request, "Tous les champs sont obligatoire")
            return redirect("loginRegister")
   
        
        if password != password1:
            messages.error(request, "les mots de passes ne correspondent pas") 
            return redirect("loginRegister")

        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Cet utilisateur existe déja")
            return redirect("loginRegister")

    
        if User.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déja utilisé")   
            return redirect("loginRegister")

        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False
        user.save()
        messages.success(request, "Succès")
        
        
        # Génération du code à 6 chiffre pour l'activation di compte
        code = rd.randint(100000, 999999)
        Profile.objects.create(user=user, code_activation=code)
        print(code)
        
        
        Objet_email = "Activation de votre Compte Rafisto.ci"
        Corps_email = render_to_string("emails/activation.html", {"username": username,
                                                                  "code": code,
                                                                #   "base_url": settings.BASE_URL,
                                                                  })
        
        
        message_email = EmailMessage(
            Objet_email, Corps_email, "agohchris90@gmail.com", [email]
        )
        message_email.content_subtype = "html"
        # message_email.connection = message_email.get_connection()
        # message_email.connection.ssl_context = ssl._create_unverified_context()
        message_email.send()
        
        messages.success(request, f"Un code d'activation a été envoyé à {email}")
        return redirect("activate")
        
            
    return render(request, "loginRegister.html")



def Activation_compte(request):
    user_email = None
    if request.method == "POST":
        email = request.POST.get("email").lower()
        code_activation = request.POST.get("activation_code")
        user_email = email
    
        try:
            # if len(code_activation) < 6:
            #     pass
            
            
            profile=Profile.objects.get(user__email=email, code_activation = code_activation
            )
            user = profile.user
            user.is_active = True
            user.save()
            profile.delete()
            
            Objet_email = "Compte Rafisto.ci activé"
            Corps_email = render_to_string("emails/valider.html", 
                                           {"username": user.username,
                                            # "base_url": settings.BASE_URL,  # Ajout de base_url
                                            })

        
            message_email = EmailMessage(
                Objet_email, Corps_email, "agohchris90@gmail.com", [email]
            )
            message_email.content_subtype = "html"
            message_email.send()

            
            messages.success(request, "Votre compte est désormais activé")
            return redirect("login")
        
        except Profile.DoesNotExist:
            messages.error(request, "Code invalide ou a expiré")
            return redirect("activate")

    return render(request, "activate.html", {"user_email": user_email})


def SignIn(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if not user.is_active:
                messages.error(request, "Votre compte n'est pas encore activé. Vérifiez votre email")
                return redirect("loginRegister")
            login(request, user)
            messages.success(request, "Connexion réussie.")
            return redirect("home")
        else:
            messages.error(request, "Erreur lor de l'authentifiaction")
              
        
    return render(request, "loginRegister.html")    



def deconnection(request):
    logout(request)
    messages.success(request,"Déconnecté")
    return render(request, "loginRegister.html")



def demamde_reinital(request):
    if request.method == "POST":
        email = request.POST.get("email").lower()

        try:
            user= User.objects.get(email=email)
            profile = Profile.objects.get(user)


            token = str(uuid.uuid4())
            profile.reset_token = token
            profile.reset_token_created_at = timezone.now()
            profile.save()

            url_de_reinitialisation = f"http://localhost:8000/reset-password/{token}/"

            Objet_email = "Réinitialisation de votre mot de passe"
            Corps_email = render_to_string("emails/mdprest.html", {
                    "username":user.username,
                    "url_de_reinitialisation" : url_de_reinitialisation
            })

            message_email = EmailMessage(
            Objet_email, Corps_email, "agohchris90@gmail.com", [email]
        )
            message_email.content_subtype = "html"
            message_email.send()


            messages.success(request, f"Un lien d'activation a été envoyé à {email}")
            return redirect("resetmsg")
        
        
        
        except User.DoesNotExist:
            messages.error(request, "Cet email n'est lié a aucun utlisateur")
            return redirect("emailenter")
        

    return render(request, "emailenter.html")



def emailenter(request):

    return render(request, "emailenter.html")


def resetpassword(request):

    return render(request, "newpass.html")


def resetmsg(request):
    return render(request, "resetmsg.html")