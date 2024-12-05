from django.shortcuts import render, redirect
from .forms import CustomUCF
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
# Register View
def register(request):
    if request.method == 'POST':
        form = CustomUCF(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration was successful, please login')
            return redirect('accounts:login')
    else:        
        form = CustomUCF()
    return render(request, 'accounts/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('myapp:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


# Logout View
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
