from django.contrib.auth import login, authenticate,forms, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect

#login_required
def main(request):
    return render(request, 'registration/main.html')

def home(request):
    return render(request,'registration/home.html')

def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request,user)
        return redirect('login')
    return render(request, 'registration/signup.html', {'form': form})

def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password.html', {
        'form': form
    })