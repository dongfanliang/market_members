#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils.encoding import smart_str, smart_unicode
import time,datetime

from apps.user.members_forms import RegisterForm,ConsumerForm
from apps.auth.static import *
from apps.models.members import Members
from apps.models.rule import Proportional

a = ['正常', '锁定','挂失']

def members_list(request):
    members = Members.objects.using('users').all()
    return render_to_response('members_list.html',{'members':members,'user':request.session[USERNAME]})


def members_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            anniversary = info['member_createtime'] + datetime.timedelta(days=365)
            try:
                Members.objects.using('users').create(member_card_id = str(info['member_card_id']),member_name = info['member_name'],\
                  members_id = str(info['member_id']),member_rank = str(info['member_rank']),member_phone=info['member_phone'],member_status=info['member_status'],\
                  member_create_time = info['member_createtime'],member_end_time = anniversary, member_surplus=info['member_surplus'],member_points=info['member_points'],\
                  member_password=info['member_password1'],member_sex=info['member_sex'])
            except Exception, e:
                return render_to_response('error.html',{'error':e,'user':request.session[USERNAME]})
            return HttpResponseRedirect('/members/')
        else:    
            return render_to_response('members_register.html',{'forms':form,'user':request.session[USERNAME]})
    else:
        form = RegisterForm()
    return render_to_response('members_register.html',{'forms':form,'user':request.session[USERNAME]})

def members_delete(request):
    to_del_list = request.GET.getlist('cb')
    num = len(to_del_list)
    for i in range(num):
        try :
            Members.objects.using('users').get(id = to_del_list[i]).delete()
        except Exception,ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
    return HttpResponseRedirect('/members/')

def members_edit(request):
    if request.method == 'POST':
        member_card_id = request.POST.get('member_card_id', '')
        member_name = request.POST.get('member_name', '')
        member_password = request.POST.get('member_password2', '')
        members_id = request.POST.get('member_id','')
        member_phone = request.POST.get('member_phone','')
        member_rank = request.POST.get('member_rank', '')
        try:
            Members.objects.using('users').filter(member_card_id = member_card_id).update(member_name = member_name, member_password = member_password, members_id = members_id, member_phone = member_phone, member_rank = member_rank)
        except Exception,ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
        return HttpResponseRedirect('/members/')
    else:
        edit_item = request.GET.get('cb', '')
        try:
            member  = Members.objects.using('users').get(id = edit_item)
        except Exception, ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
    return render_to_response('member_edit.html',{'member':member,'user':request.session[USERNAME]})
   
def members_search(request):
    if request.method == 'POST':
       card_id = request.POST.get('list_search')
       mem_rank = request.POST.get('mem_rank')
       mem_name = request.POST.get('mem_name')
       print mem_name, mem_rank, card_id
       if smart_str(card_id) !='会员卡号':
           if mem_rank != 'all':
               if mem_name != '':
                   results = Members.objects.using('users').filter(member_card_id__contains=card_id, member_name__contains=mem_name, member_rank__contains=mem_rank)
               else:
                   results = Members.objects.using('users').filter(member_card_id__contains=card_id, member_rank__contains=mem_rank)
           else:
               if mem_name != '':
                   results = Members.objects.using('users').filter(member_card_id__contains=card_id, member_name__contains=mem_name)
               else:
                   results = Members.objects.using('users').filter(member_card_id__contains=card_id)                   
       else:
           if mem_rank != 'all':
               if mem_name != '':
                   results = Members.objects.using('users').filter(member_name__contains=mem_name, member_rank__contains=mem_rank)
               else:
                   results = Members.objects.using('users').filter(member_rank__contains=mem_rank)
           else: 
               if mem_name != '':
                   results = Members.objects.using('users').filter(member_name__contains=mem_name)
               else:
                   results = Members.objects.using('users').all()
    return render_to_response('members_list.html',{'members':results, 'user':request.session[USERNAME]})

def rule(request):
    return render_to_response('rule.html',{'user':request.session[USERNAME]})

def member_rule(request):
    return render_to_response('mem_rule.html',{'user':request.session[USERNAME]})
    
def cards_list(request):
    members = Members.objects.using('users').all()
    for i in members:
        i.member_status = a[int(i.member_status) - 1]
    return render_to_response('members_cards.html',{'members':members,'user':request.session[USERNAME]})

def cards_rechange(request):
    if request.method == 'POST': 
        member_card_id = request.POST.get('member_card_id', '')
        member_name = request.POST.get('member_name', '')
        rechange = request.POST.get('rechange','')
        if rechange == '':
            return HttpResponseRedirect('/cards/')
        n = Members.objects.using('users').get(member_card_id=member_card_id,member_name=member_name)
        count = float(rechange) + n.member_surplus
        Members.objects.using('users').filter(member_card_id=member_card_id,member_name=member_name).update(member_surplus=count)
        return HttpResponseRedirect('/cards/')
    else:
        edit_item = request.GET.get('cb', '')
        try:
            member  = Members.objects.using('users').get(id = edit_item)
        except Exception, ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
    return render_to_response('rechange.html',{'member':member,'user':request.session[USERNAME]})
#延长有效期
def cards_v(request):
    to_del_list = request.GET.getlist('cb')
    num = len(to_del_list)
    for i in range(num):
        try :
            result = Members.objects.using('users').get(id = to_del_list[i])
            v = result.member_end_time + datetime.timedelta(days=365)
            Members.objects.using('users').filter(id = to_del_list[i]).update(member_end_time = v)
        except Exception,ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
    return HttpResponseRedirect('/cards/')

#挂失
def cards_loss(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        try:
            result = Members.objects.using('users').get(members_id = member_id)
        except Exception:
            error_m = "该用户不存在 !"
            return  render_to_response('cards_loss.html',{'error':error_m,'user':request.session[USERNAME]})
        Members.objects.using('users').filter(members_id = member_id).update(member_status = '3')
        return HttpResponseRedirect('/cards/')
    else:        
        return render_to_response('cards_loss.html',{'user':request.session[USERNAME]})

#补办
def cards_retroactive(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        card_id = request.POST.get('member_card_id')
        if len(card_id) != 10:
            error_m = '卡号输入错误!'
            return render_to_response('cards_retroactive.html',{'error':error_m,'user':request.session[USERNAME]})
        try:
            Members.objects.using('users').filter(members_id = member_id).update(member_card_id = card_id, member_status = '1')
        except Exception:
            error_m = '该用户不存在 !'
            return  render_to_response('cards_retroactive.html',{'error':error_m,'user':request.session[USERNAME]})
        return HttpResponseRedirect('/cards/')
    else:
        return render_to_response('cards_retroactive.html',{'user':request.session[USERNAME]})
      
    
def cards_search(request):
    if request.method == 'POST':
       card_id = request.POST.get('list_search')
       mem_status = request.POST.get('mem_status')
       mem_name = request.POST.get('mem_name')
       print mem_name, mem_status, card_id
       if smart_str(card_id) !='会员卡号':
           if mem_status != 'all':
               if mem_name != '':
                   results = Members.objects.using('users').filter(member_card_id__contains=card_id, member_name__contains=mem_name, member_status__contains=mem_rank)

               else:
                   results = Members.objects.using('users').filter(member_card_id__contains=card_id, member_status__contains=mem_status)
           else:
               if mem_name != '':
                   results = Members.objects.using('users').filter(member_card_id__contains=card_id, member_name__contains=mem_name)
               else:
                   results = Members.objects.using('users').filter(member_card_id__contains=card_id)                   
       else:
           if mem_status != 'all':
               if mem_name != '':
                   results = Members.objects.using('users').filter(member_name__contains=mem_name, member_status__contains=mem_status)
               else:
                   results = Members.objects.using('users').filter(member_status__contains=mem_status)
           else: 
               if mem_name != '':
                   results = Members.objects.using('users').filter(member_name__contains=mem_name)
               else:
                   results = Members.objects.using('users').all()
    for i in results:
            i.member_status = a[int(i.member_status) - 1]
    return render_to_response('members_cards.html',{'members':results, 'user':request.session[USERNAME]})

def cards_s(request):
    if request.method == 'POST':
        card = request.POST.get('cardid')
        try:
            result = Members.objects.using('users').get(member_card_id=card)
        except Exception,ex:
            error_m = "该会员不存在 !"
            return render_to_response('cards_consume.html',{'error':error_m,'user':request.session[USERNAME]})
    #print type(str(result.member_end_time)), type(str(time.strftime("%Y-%m-%d",time.localtime())))
    #print str(result.member_end_time) < str(time.strftime("%Y-%m-%d",time.localtime()))
    
    if str(result.member_end_time) < time.strftime("%Y-%m-%d",time.localtime()):
        error_m = '该会员已过期,请续期!'
        Members.objects.using('users').filter(member_card_id=card).update(member_status = '1')
        return render_to_response('cards_consume.html',{'error':error_m,'types':types,'member':result,'user':request.session[USERNAME]})
    else:
        types = Proportional.objects.using('rule').all()
        result.member_status = a[int(result.member_status) - 1]
    return render_to_response('cards_consume.html',{'types':types,'member':result,'user':request.session[USERNAME]})


def cards_consume(request):
    typesall = Proportional.objects.using('rule').all()
    if request.method == 'POST':
        member_name = request.POST.get('name')
        member_points = request.POST.get('points') 
        if member_name == '':
            error_m = '请输入会员卡号 !'
            return render_to_response('cards_consume.html',{'types':typesall,'error':error_m,'user':request.session[USERNAME]})
        result = Members.objects.using('users').get(member_name = member_name, member_points = member_points)
        money = request.POST.get('price')
        method = request.POST.get('method')
        types = request.POST.get('types')

        if result.member_status == '1':
            result.member_status = a[int(result.member_status) - 1]   
            if int(method) == 0:
                if result.member_surplus < float(money):
                    error_m = '卡内余额不足 !'
                    return render_to_response('cards_consume.html',{'types':typesall,'price':money,'member':result,'error_m':error_m,'user':request.session[USERNAME]})
                else:
                    if types == "0":
                        result.member_surplus  -= float(money)
                    else:
                        result.member_surplus  -= float(money)
                        pro = Proportional.objects.using('rule').get(id = types)
                        l = pro.proportion.split("/") 
                        m = int(l[0])
                        p = int(l[1])
                        result.member_points = result.member_points + float(money) * p / m
                        Members.objects.using('users').filter(member_name = member_name, member_points = member_points).update(member_surplus = result.member_surplus, member_points = result.member_points)
                    return HttpResponseRedirect("/cards")
            else:
                if types != "0":
                    pro = Proportional.objects.using('rule').get(id = types)
                    l = pro.proportion.split("/")
                    m = int(l[0])
                    p = int(l[1])
                    result.member_points = result.member_points + float(money) * p / m
                    Members.objects.using('users').filter(member_name = member_name, member_points = member_points).update(member_points = result.member_points)
            return HttpResponseRedirect("/cards")
        else:      
            error_m = '该会员卡处于非正常状态 !'
            return render_to_response('cards_consume.html',{'error_m':error_m,'user':request.session[USERNAME]})
    return render_to_response('cards_consume.html',{'types':typesall,'user':request.session[USERNAME]})
