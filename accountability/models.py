from django.db import models
from django.conf import settings

class Penalty(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='penalties')
    missed_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)
    reason = models.TextField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.missed_date} - {self.amount}"
