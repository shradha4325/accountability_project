from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome {user.username}! Your account has been created.")
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})

@login_required
def find_partner(request):
    search_query = request.GET.get('q', '')
    users = CustomUser.objects.filter(username__icontains=search_query).exclude(id=request.user.id).exclude(partner__isnull=False)
    return render(request, 'users/find_partner.html', {'users': users, 'query': search_query})

@login_required
def connect_partner(request, partner_id):
    partner = get_object_or_404(CustomUser, id=partner_id)
    if not request.user.partner and not partner.partner:
        # For simplicity in this demo, we auto-connect. In a real app, use a Request model.
        request.user.partner = partner
        partner.partner = request.user
        request.user.save()
        partner.save()
        messages.success(request, f"You are now connected with {partner.username}!")
    return redirect('dashboard')

@login_required
def disconnect_partner(request):
    if request.user.partner:
        partner = request.user.partner
        # Disconnect both sides
        request.user.partner = None
        partner.partner = None
        request.user.save()
        partner.save()
        messages.success(request, f"You have disconnected from {partner.username}.")
    return redirect('dashboard')
