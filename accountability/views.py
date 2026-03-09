from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Penalty
from django.utils import timezone
from progress.models import Progress
from django.contrib import messages

@login_required
def penalty_list(request):
    penalties = Penalty.objects.filter(user=request.user).order_by('-missed_date')
    total_penalty = sum(p.amount for p in penalties if not p.is_paid)
    return render(request, 'accountability/penalty_list.html', {
        'penalties': penalties,
        'total_penalty': total_penalty
    })

# In a real app, this would be a management command run by a celery beat / cron job
def check_missed_days(user):
    today = timezone.now().date()
    yesterday = today - timezone.timedelta(days=1)
    
    # Check if user logged anything yesterday
    if not Progress.objects.filter(user=user, date=yesterday).exists():
        # Create penalty if not already exists
        if not Penalty.objects.filter(user=user, missed_date=yesterday).exists():
            Penalty.objects.create(
                user=user,
                missed_date=yesterday,
                amount=50.00,
                reason="Missed daily progress log"
            )
            return True
    return False
