from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm, AuthenticationForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class Registration(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html', {"form": form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            try:
                error = form.errors.get("email").as_text()
                if error == '* User with this Email address already exists.':
                    messages.add_message(request, messages.INFO, 'You are already registered ')
                    return render(request, 'registration.html', {'form':form})
                return render(request, 'registration.html', {'form':form}) 
            except:    
                return render(request, 'registration.html', {'form':form})


class LoginUser(View):
    def get(self,request):
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        form =AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            print(form.errors)
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(email=uname,password=upass)
            if user :
                login(request,user)
                return redirect('home')
        else:
            return render(request,'login.html', {'form':form})

class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect("/")            