from auth import views
from django.urls import path


urlpatterns = [
    path("home/", views.home(), name="home"),
    path("register/", views.register, name="register"),
    path("/", views.SignIn, name="login"),
]



email = nzfz yelo yjwh ruzd




 "auth",



     "default":{
        "ENGINE": "mysql.connector.django",
        "NAME": "authEnter",
        "USER":"root",
        "PASSWORD":"",
        "HOST":"localhost",
        "PORT":"3306",   
    },

{% if active_form == 'register' %}active{% endif %}

{% if active_form == 'login' %}active{% endif %}








from django.shortcuts import render




# Create your views here.


def home(request):
    
    return render(request, "home.html")



def register(request):
    
    return render(request, "register.html")




def SignIn(request):
    
    
    
    return render(request, "login.html")    



path("", include("auth.urls"))















        .messages {
            margin-bottom: 20px;
            padding: 10px;
            border-radius: 5px;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
    
        .message {
            margin: 0;
            padding: 5px 0;
        }
    
        .message.success {
            background-color: #d4edda;
            color: #155724;
            border-color: #c3e6cb;
        }
    
        .message.error {
            background-color: #f8d7da;
            color: #721c24;
            border-color: #f5c6cb;
        }
    
        .message.info {
            background-color: #d1ecf1;
            color: #0c5460;
            border-color: #bee5eb;
        }
    
        .message.warning {
            background-color: #fff3cd;
            color: #856404;
            border-color: #ffeeba;
        }






   {% if messages %}
        <div class="messages">
            {% for message in messages %}
                <p class="message {{ message.tags }}">{{ message }}</p>
            {% endfor %}
        </div>
    {% endif %}





    <h1>Bonjour {{ user.username }} </h1>
    <p>Bienvenue sur la page d'accueil de l'application sécurisée.</p>

    <p>Voici quelques informations sur votre compte :</p>
    <ul>
        <li>Nom d'utilisateur : {{ user.username }}</li>
        <li>Email : {{ user.email }}</li>
        <li>Date de création du compte : {{ user.date_joined }}</li>
    </ul>
    <a href="{% url 'logout' %}">Logout</a>


                    <!-- <li><a href="{% url 'loginRegister' %}" class="nav__cta">Sign up</a></li> -->
