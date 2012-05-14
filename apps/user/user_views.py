#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from apps.models.user_models import User
from apps.auth.auth import *
from apps.auth.static import *
from apps.user.user_forms import UserForm 
from django.utils.encoding import smart_str, smart_unicode


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        print username, password
        error_m = "Wrong User Name or Password!"
        if username == '' or password == '':
            return render_to_response('login.html',{'error':error_m,'username':'', 'password':''})
        u = authenticated(username, password)    
        if u == False:
            return render_to_response('login.html',{'error':error_m,'username':'', 'password':''})
        else:
            request.session[USERNAME] = username
            request.session[PASSWORD] = password
            return HttpResponseRedirect('/index/') 
    else:
        return render_to_response('login.html',{'username':'', 'password':''})

def index(request):
    return render_to_response('index.html', {'user':request.session[USERNAME]})

def getpassword(request):
    return render_to_response('get_password.html', {'flag':0})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login')

def userinfo(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        extra = request.POST.get('extra', '')
        branch = request.POST.get('branch', '')
        branch_address = request.POST.get('branch_address', '')
        user = User.objects.using('default').filter(username = username).update(password=password,email=email,extra=extra,branch=branch,branch_address = branch_address)
        return HttpResponseRedirect('/index/')
    else:
        username = request.session[USERNAME]
        user = User.objects.using('default').get(username = username)
    return render_to_response('user_info.html', {'use':user,'user':request.session[USERNAME]})

def user_list(request):
    users = User.objects.using('default').all()
    return render_to_response('users.html', {'users':users,'user':request.session[USERNAME]})

def user_add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            try:
                User.objects.using('default').create(username=str(info['user_name']), password=info['user_password1'],email=info['user_email'],branch=info['user_branch'],branch_address=info['user_branch_address'],extra=info['user_extra'])
            except Exception, e:
                return render_to_response('error.html',{'error':e,'user':request.session[USERNAME]})
            return HttpResponseRedirect('/user/')
    else:     
        form = UserForm()
    return render_to_response('user_add.html', {'forms':form,'user':request.session[USERNAME]})
    
def user_delete(request):
    to_del_list = request.GET.getlist('cb')
    num = len(to_del_list)
    for i in range(num):
        try:
            User.objects.using('default').get(id = to_del_list[i]).delete()
        except Exception,ex:  
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
    return HttpResponseRedirect('/user/')

def user_search(request):
    if request.method == 'POST':
        username = request.POST.get('list_search')
        if smart_str(username) == '用户名':
            return HttpResponseRedirect('/user/')
        result = User.objects.using('default').filter(username__contains = smart_str(username))
    return render_to_response('users.html', {'users':result,'user':request.session[USERNAME]})

