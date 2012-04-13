from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from apps.auth.auth import *
from apps.auth.static import *
#from apps.user.user_forms import RegisterForm

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
    
