from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from .forms import SignupForm,EditProfileForm,EditUserForm
from .models import Profile
# Create your views here.
def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid:
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('jobs/')
        else:
            return redirect()
    else:
        form=SignupForm()
    return render(request,'registration/signup.html',{'form':form})


def viewprofile(request,slug):
    profile=Profile.objects.get(slug=slug)
    return render(request,'accounts/profile.html',{'profile':profile})
def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})
def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
         userform=EditUserForm(request.POST,request.FILES,instance=request.user)
         profileform=EditProfileForm(request.POST,request.FILES,instance=profile)
         if userform.is_valid and profileform :
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            userform.save()
            return redirect(reverse('accounts:profile'))
            
    else:
         userform=EditUserForm(instance=request.user)
         profileform=EditProfileForm(instance=profile)
    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})
    
def logout_view(request):
    logout(request)