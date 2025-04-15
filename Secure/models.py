from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code_activation = models.CharField(max_length=6, unique=True)


    # Code envoyé par mail pour la réinitialisation
    reset_code = models.CharField(max_length=6, blank=True, null=True)
    reset_code_created_at = models.DateTimeField(blank=True, null=True)
    
    # Pour savoir si le code à 6 chiffres a bien été validé
    code_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} - {self.code_activation}"

    def is_code_valid(self):
        """Vérifie si le code est encore valide (10 minutes par exemple)"""
        if self.reset_code_created_at:
            return timezone.now() < self.reset_code_created_at + timedelta(minutes=5)
        return False