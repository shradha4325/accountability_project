from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Progress
from .forms import ProgressForm
from django.utils import timezone
from users.models import CustomUser

@login_required
def log_progress(request):
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.user = request.user
            progress.save()
            messages.success(request, "Progress logged successfully!")
            return redirect('dashboard')
    else:
        form = ProgressForm()
    return render(request, 'progress/log_progress.html', {'form': form})

@login_required
def partner_progress_view(request, username):
    partner = get_object_or_404(CustomUser, username=username)
    # Check if they are actually partners
    if request.user.partner != partner:
        messages.error(request, "This user is not your accountability partner.")
        return redirect('dashboard')
    
    progress_logs = Progress.objects.filter(user=partner).order_by('-date')
    return render(request, 'progress/partner_view.html', {'partner': partner, 'progress_logs': progress_logs})
