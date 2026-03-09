from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Goal
from .forms import GoalForm
from progress.models import Progress

@login_required
def dashboard(request):
    goals = Goal.objects.filter(user=request.user)
    recent_progress = Progress.objects.filter(user=request.user).order_by('-date')[:5]
    
    partner_progress = []
    if request.user.partner:
        partner_progress = Progress.objects.filter(user=request.user.partner).order_by('-date')[:5]

    context = {
        'goals': goals,
        'recent_progress': recent_progress,
        'partner': request.user.partner,
        'partner_progress': partner_progress,
    }
    return render(request, 'goals/dashboard.html', context)

@login_required
def create_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, "Goal created successfully!")
            return redirect('dashboard')
    else:
        form = GoalForm()
    return render(request, 'goals/create_goal.html', {'form': form})
