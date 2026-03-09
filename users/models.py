from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    partner = models.OneToOneField(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='accountability_partner'
    )
    skills_to_learn = models.TextField(blank=True, help_text="Comma-separated skills")

    def __str__(self):
        return self.username
