from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
import csv
import json
from django.views import View
import os
from uuid import uuid4
from django.utils import timezone

# Create your views here.

# <a href="{% url 'profile_list' %}">프로필 보기</a>
# urls.py
# def profile_list():
#   DB
#   context = {'key': value}
#   return render('xxxxx.html' , context)
# xxxx.html -> {{xxxx.id}}

def index(request) :
    if request.session.get('user_name') :
        context={id: request.session['user_name']
                 }
        return render(request, 'home2.html', context)
    else :
        return render(request, 'page-login2.html')

def registerForm2(request) :
    return render(request, 'page-register2.html')

def register(request) :
    if request.method == 'POST':
        name = request.POST['id']
        pwd = request.POST['pwd']
        email = request.POST['email']
        value_bio = request.POST['bio']
        value_contact= request.POST['contact']
        value_location= request.POST['location']

        register111 = User(username=name, password=pwd, email=email)
        register111.save()

        re = StuProfile.objects.get(user_name=name)
        re.bio = value_bio
        re.contact= value_contact
        re.location= value_location
        re.save()

    return render(request, 'page-login2.html')

def logout(request) :
    request.session['user_name'] = {}
    request.session.modified= True
    return redirect('index')

def loginForm(request) :
    return render(request, 'page-login2.html')

def login(request) :
    if request.method== 'GET' :
        return redirect('index')

    elif request.method=='POST' :
        id = request.POST['id']
        pwd= request.POST['pwd']

        user=User.objects.get(username= id, password=pwd)

        context= {}
        if user is not None:
            request.session['user_name'] = user.username

            context['id'] = request.session['user_name']

            print('로그인 시 세션 정보 뭐뭐 넘어가나. 확인-', context)
            return render (request, 'home2.html', context)

        else :
            return redirect('index')

#-----------------------------------------------------------

def profile_list(request) :
    readusers= StuProfile.objects.all()

    context={'readusers' : readusers,
             'id' : request.session['user_name']}
    print('request - ' , readusers)

    return render(request, 'lists2.html', context)

#------------------------------------------------------------
def profile_read2(request, id) :
    read_stu= StuProfile.objects.get(id=id)
    print('아이디체크', id)
    read_user= User.objects.get(username=read_stu.user_name)
    context = {'readpro': read_user,
               'readpro2' : read_stu,
               'id' : request.session['user_name']
               }
    print('확인...', context)
    return render(request, 'readcon2.html', context)
#-------------------------------------------------------

def modify_form(request) :
    id= request.POST['id']
    print('수정 폼에서 받아오는 id는?', id)

    read_one= StuProfile.objects.get(id=id)
    read_two= User.objects.get(username=read_one.user_name)

    context= {'readmodi' : read_two,
              'readmodi2' : read_one,
              'id' : request.session['user_name']
              }

    print('컨텍스트 확인-', context)

    return render(request, 'profile_modify2.html', context)

# ㄻㄴㅇㄹㅇㄹ
#---------------------------------------------------------
def profile_modify(request) :

    id= request.POST['id']
    user_name= request.POST['user_id']
    bio= request.POST['mybio2']
    contact=request.POST['contact']
    location=request.POST['location']

    print('수정 중 값 확인...', id, user_name, bio, contact, location)

    readmodi= StuProfile.objects.get(id=id)

    readmodi.bio= bio
    readmodi.contact=contact
    readmodi.location=location

    readmodi.save()

    return redirect('stuApp:profile_list')

#------------------------------------------
def attachPhoto(request) :
    profile_photo= request.FILES['profile_photo']

    if not profile_photo.name.endswith('.png') and ('jpg') :
        return redirect('index')

#---------------------------------------------------
def profile_read(request, id) :
    readpro= User.objects.get(id=id)
    # test1= readpro.username
    #print('read img - ', readpro.profile_img)
    print('read시 넘어가는 정보는? - ' , readpro)

    #readpro2 = StuProfile.objects.all()
    readpro2= StuProfile.objects.get(user_name=readpro.username)

    # readpro2= StuProfile.objects.get(user_name=readpro.username)

    context = {'readpro': readpro,
               'readpro2' : readpro2,
               'id': request.session['user_name']
               }

    return render(request, 'readcon2.html', context)