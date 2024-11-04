from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import (LoginForm, UserRegistrationForm, UserEditForm,ProfileEditionForm)
from .models import Profile

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditionForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success( request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
            return redirect('dashboard')  # Redirect to a success page, e.g., the dashboard
    else:
        # Initial GET request to render the form
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditionForm(instance=request.user.profile)
    
    # Render the form for both GET and invalid POST requests
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'} )
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the user object
            new_user.save()
            #create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()  # This initializes the form for GET requests

    # Return the registration form for both GET and invalid POST requests
    return render(request, 'account/register.html', {'user_form': user_form})
