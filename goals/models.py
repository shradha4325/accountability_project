from django.db import models
from django.conf import settings

class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='goals')
    skill_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    daily_target = models.PositiveIntegerField(help_text="Target hours per day")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.skill_name}"
