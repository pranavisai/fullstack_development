from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def user_logout(request):
    # logs out the user
    logout(request) 
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if(request.method == "POST"):
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if(user_form.is_valid() and profile_form.is_valid()):

            user = user_form.save() #grabbing the userform and setting it into the database
            user.set_password(user.password) #hashing the password with the set_password method
            user.save() #then we are saving the hashed passwords to the database

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()   
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}) 

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) #this will authenticate the user automatically

        if(user):
            if user.is_active:
                login(request, user) #if the user is active then pass in the user object returned by the above authenticate function
                return HttpResponseRedirect(reverse('index')) #to redirect back to the home page because of the reverse function
            
            else:
                return HttpResponse("Account not active")
            
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied")
    
    else:
        return render(request, 'basic_app/login.html', {})
