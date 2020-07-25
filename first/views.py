# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from first.models import images, ques_ans
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def handler500(request):
    return redirect('logout')

@login_required(login_url='login')
def ans(request, ques_id):
    if request.method=='POST':
        ans = request.POST['ans']
        username = user.username
        a = ques_ans.objects.filter(username = username, ques_id = ques_id)
        a.update(ans = ans)
        return redirect('/')

def ask(request, username):
    if request.method=='POST':
        b = ques_ans.objects.filter(username = username)
        x = len(b)
        a = ques_ans()
        a.username = username
        a.ques_id = x
        question = request.POST['ques']
        a.ques = question
        a.save()
        url = "/"+username+"/"
        return redirect(url)

@login_required(login_url='login')
def dlt(request, ques_id):
    username = user.username
    a = ques_ans.objects.filter(username = username, ques_id = ques_id)
    a.update(ans = None)
    return redirect('/')

def show(request, username):
    a = images.objects.filter(username=username)
    if not a:
        return HttpResponse("No such user")
    if a[0].profile:
        profile = a[0].profile.url
    else:
        profile = None
    if a[0].image1:
        image1 = a[0].image1.url
    else:
        image1 = None
    if a[0].image2:
        image2 = a[0].image2.url
    else:
        image2 = None
    if a[0].image3:
        image3 = a[0].image3.url
    else:
        image3 = None
    if a[0].image4:
        image4 = a[0].image4.url
    else:
        image4 = None
    b = ques_ans.objects.filter(username=username)
    x = User.objects.filter(username=username)
    name = x[0].first_name+" "+x[0].last_name
    dic = {'profile' : profile, 'image1' : image1, 'image2' : image2, 'image3' : image3, 'image4' : image4, 'ques_ans' : b,'name' : name}
    return render(request,"show.html",context=dic)

@login_required(login_url='login')
def index(request):
    username = user.username
    a = images.objects.filter(username=username)
    if a[0].profile:
        profile = a[0].profile.url
    else:
        profile = None
    if a[0].image1:
        image1 = a[0].image1.url
    else:
        image1 = None
    if a[0].image2:
        image2 = a[0].image2.url
    else:
        image2 = None
    if a[0].image3:
        image3 = a[0].image3.url
    else:
        image3 = None
    if a[0].image4:
        image4 = a[0].image4.url
    else:
        image4 = None
    b = ques_ans.objects.filter(username=username)
    c = "harshsingh.pythonanywhere.com/"+username
    dic = {'profile' : profile, 'image1' : image1, 'image2' : image2, 'image3' : image3, 'image4' : image4,'ques_ans' : b, 'profile_id' : c}
    return render(request,"index.html",context=dic)

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        global user
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid login')
            return redirect('login/')
    return render(request, 'login.html')

def reg(request):
    a = images()
    if request.method=="POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password1"]
        password2 = request.POST["password2"]
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register/')
            else:
                user = User.objects.create_user(username = username, password=password,first_name=first_name,last_name=last_name)
                user.save()
                a.username = username
                a.save()
                return redirect('login')
        else:
            messages.info(request,'Password Mismatch')
            return redirect('register')
    return render(request, 'reg.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    username = user.username
    s = images.objects.filter(username=username)
    if request.method == "POST":
        profile = request.FILES['profile']
        a = images(username=username,profile=profile, image1=s[0].image1, image2=s[0].image2,image3=s[0].image3, image4=s[0].image4)
        a.save()
        return redirect('/')

@login_required(login_url='login')
def image1(request):
    username = user.username
    s = images.objects.filter(username=username)
    if request.method == "POST":
        image1 = request.FILES['image1']
        a = images(username=username,profile=s[0].profile, image1=image1, image2=s[0].image2,image3=s[0].image3, image4=s[0].image4)
        a.save()
        return redirect('/')

@login_required(login_url='login')
def image2(request):
    username = user.username
    s = images.objects.filter(username=username)
    if request.method == "POST":
        image2 = request.FILES['image2']
        a = images(username=username,profile=s[0].profile, image1=s[0].image1, image2=image2,image3=s[0].image3, image4=s[0].image4)
        a.save()
        return redirect('/')

@login_required(login_url='login')
def image3(request):
    username = user.username
    s = images.objects.filter(username=username)
    if request.method == "POST":
        image3 = request.FILES['image3']
        a = images(username=username,profile=s[0].profile, image1=s[0].image1, image2=s[0].image2,image3=image3, image4=s[0].image4)
        a.save()
        return redirect('/')

@login_required(login_url='login')
def image4(request):
    username = user.username
    s = images.objects.filter(username=username)
    if request.method == "POST":
        image4 = request.FILES['image4']
        a = images(username=username,profile=s[0].profile, image1=s[0].image1, image2=s[0].image2,image3=s[0].image3, image4=image4)
        a.save()
        return redirect('/')