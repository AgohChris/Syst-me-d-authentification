from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import random as rd
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.urls import reverse
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

    
        # if User.objects.filter(email=email).exists():
        #     messages.error(request, "Cet email est déja utilisé")   
        #     return redirect("loginRegister")

        
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





#Section de Reinitialisation

def demande_reset_mot_de_passe(request):
    if request.method == "POST":
        email = request.POST.get("email").lower()

        try:
            user = User.objects.get(email=email)
            profile = Profile.objects.get(user=user)

            # Générer un code à 6 chiffres
            code = str(rd.randint(100000, 999999))
            profile.reset_code = code
            profile.reset_code_created_at = timezone.now()
            profile.code_verified = False  # Remise à zéro
            profile.save()

            # Email de réinitialisation
            objet_email = "Réinitialisation de votre mot de passe"
            corps_email = render_to_string("emails/code_reinitialisation.html", {
                "username": user.username,
                "code": code,
            })

            message_email = EmailMessage(
                objet_email,
                corps_email,
                "agohchris90@gmail.com",
                [email]
            )
            message_email.content_subtype = "html"
            message_email.send()

            messages.success(request, f"Un code à 6 chiffres a été envoyé à {email}")
            return redirect("verification_code_reset", email=email) 

        except User.DoesNotExist:
            messages.error(request, "Aucun compte n’est associé à cet email.")
            return redirect("demande_reset_password")

    return render(request, "Verifmail.html")




def verification_code_reset(request, email):
    
    try:
        user = User.objects.get(email=email)
        profile = Profile.objects.get(user=user)
    except (User.DoesNotExist, Profile.DoesNotExist):
        messages.error(request, "L'utilisateur est introuvable .")
        return redirect("demande_reset_password")
    

    if request.method == "POST":
        code_saisi = request.POST.get("code")

        if not profile.reset_code:
            messages.error(request, "Aucun code n'a été générer pour  cette adresse .")
            return redirect("demande_reset_password")
        
        if not profile.is_code_valid():
            messages.error(request, "Le code a expirer. Veuillez refaire votre demande.")
            return redirect("demande_reset_password")
        
        if code_saisi != profile.reset_code:
            messages.error(request, "le code saisi est invalide.")
            return redirect("verification_code_reset", email=email)
        

        # Si tout est alors on le laisse 
        profile.code_verified = True
        profile.save()
        return redirect("changement_password", email=email)
    
    
    return render(request, "verif_code_reset.html", {"email": email})
    



def Changement_de_mot_de_passe(request, email):
    try:
        user = User.objects.get(email=email)
        profile = Profile.objects.get(user=user)
        
    except (User.DoesNotExist, Profile.DoesNotExist):
        messages.error(request, "L'utilisateur est introuvable")
        return redirect("loginRegister")
    
    if not profile.code_verified:
        messages.error(request, "Le code est non verifier. Recomncencer tout ")
        return redirect("demande_reset_password")
    

    if request.method == "POST":
        mdp = request.POST.get("password")
        mdp1 = request.POST.get("password1")

        if mdp != mdp1 :
            messages.error(request, "Les mots de passe ne correspondent pas")
            return redirect("changement_password", email=email)
        

        #Verification de la securite du mdp
        if len(mdp) < 6:
            messages.error(request, "Le mot de passe doit contenir au moins 6 caractères")
       
        elif not any(char.isdigit() for char in mdp):
            messages.error(request, "Le mot de passe doit contenir au moins 1 chiffre")

        elif not any(char.isalpha() for char in mdp):
            messages.error(request, "Le mot de passe doit contenir au moins une lettre")
        
        else:
            user.password = make_password(mdp)
            user.save()


            #Reinitialisation du profile
            profile.reset_code = None
            profile.reset_code_created_at = None
            profile.code_verified = False
            profile.save()


            #confirmReset.html

            #Envoie du mail de confirmation 

            Objet_email = "Mot de passe reinitialisé"
            Corps_email = render_to_string("emails/code_reinitialisation.html", {"username": user.username,
                                                                  })
        
        
            message_email = EmailMessage(
                Objet_email, Corps_email, "agohchris90@gmail.com", [email]
            )
            message_email.content_subtype = "html"
            message_email.send()

            messages.success(request, "Le Mot de passe est reset. vous pouvez vous connecter")
            return redirect("loginRegister")
    

    return render(request, "nouveauMdp.html", {"email": email})

        
