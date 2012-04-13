#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from apps.user.members_forms import RegisterForm
from apps.auth.static import *
from apps.models.members import Members

def members_list(request):
    members = Members.objects.using('default').all()
    return render_to_response('members_list.html',{'members':members,'user':request.session[USERNAME]})

def members_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            try:
                Members.objects.using('default').create(member_card_id = str(info['member_card_id']),member_name = str(info['member_name']),\
                  members_id = str(info['member_id']),member_rank = str(info['member_rank']),member_phone=info['member_phone'],member_status=info['member_status'],\
                  member_create_time = info['member_createtime'],member_surplus=info['member_surplus'],member_points=info['member_points'],\
                  member_password=info['member_password2'],member_sex=info['member_sex'])
            except Exception, e:
                return render_to_response('error.html',{'error':e,'user':request.session[USERNAME]})
            return HttpResponseRedirect('/members/')
        else:    
            return render_to_response('members_register.html',{'forms':form,'user':request.session[USERNAME]})
    else:
        form = RegisterForm()
    return render_to_response('members_register.html',{'forms':form,'user':request.session[USERNAME]})

def members_delete(request):
    to_del_list = request.POST.getlist('cb')
    num = len(to_del_list)
    for i in range(num):
        try :
            Members.objects.using('default').get(id = to_del_list[i]).delete()
        except Exception,ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
    return HttpResponseRedirect('/members/')

#def member_edit(request):
    
