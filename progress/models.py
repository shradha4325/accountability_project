from django.db import models
from django.conf import settings
from goals.models import Goal

class Progress(models.Model):
    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Incomplete', 'Incomplete'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progress_logs')
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='progress_entries')
    date = models.DateField(auto_now_add=True)
    topic = models.CharField(max_length=255)
    time_spent = models.DecimalField(max_digits=4, decimal_places=2, help_text="Hours spent")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Completed')

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.topic}"
