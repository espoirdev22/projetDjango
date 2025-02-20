from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from .models import User

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Vérifier si l'utilisateur existe
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            # Vérifier si le nom d'utilisateur existe
            if not User.objects.filter(username=username).exists():
                # Si l'utilisateur n'existe pas, rediriger vers la page d'inscription
                return redirect('register')
            else:
                # Si l'utilisateur existe mais le mot de passe est incorrect
                error = 'Mot de passe incorrect'
    
    return render(request, 'login.html', {'error': error})

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})