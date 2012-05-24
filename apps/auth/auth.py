#!/usr/bin/python
#codeing=utf-8
from apps.models.user_models import User
from apps.auth.static import *

def exit_username(username):
    """
    test the username whether exit
    if exit return true else false
    """ 
    user = User.objects.using('users').get(username=username)
    if user == None:
        return False
    else:
        return True

def checkpassword(username, password):
    password = str(password)
    user = authenticated(str(username), password)
    return user

def authenticated(username, password):
    try:
        user = User.objects.using('users').get(username=str(username), password=str(password))
    except User.DoesNotExist:
        return False
    else:
        return True

def resetpassword(username, password):
    """
    update the user password
    """
    pass

def logout(request):
    user = None
    try:
        request.session.flush()
    except Exception,e:
        error_m = "Failed to Logout, please try again!"
        return error_m

def login(request, user):
    try:
        request.session[USERNAME] = user.user_userName
        request.session[ISADMIN] = user.user_admin
    except Exception,e:
        error_m = _("User Not Exist !")
        return error_m
