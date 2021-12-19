from django.contrib.auth import authenticate
from django.shortcuts import render
from users import forms
from users import models
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib import auth
from django.http import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
import datetime;

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                
                return redirect("post")
            else:
                HttpResponse(request,"Invalid username or password.")
        else:
            HttpResponse(request,"Invalid username or password.")
    form = AuthenticationForm()
    
    return render(request,'home.html',{'form':form})
@login_required

def post(request):
    
    ct = datetime.datetime.now()
    form = forms.PostData()
    if request.method == "POST":
        form = forms.PostData(request.POST)
        if form.is_valid():
            models.post.objects.create(user=request.user,text=form.cleaned_data['text'],created_at=ct,updated_at=ct)
            messages.success(request,'Posted successfully')
    return render(request,'post.html',{'form':form})
