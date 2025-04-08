from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Secure.urls")),
    # path('accounts/', include('allauth.urls')),
]
