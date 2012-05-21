#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils.encoding import smart_str, smart_unicode

from apps.user.members_forms import RegisterForm,ConsumerForm
from apps.auth.static import *
from apps.models.members import Members

a = ['正常', '锁定','挂失']
def members_list(request):
    members = Members.objects.using('default').all()
    return render_to_response('members_list.html',{'members':members,'user':request.session[USERNAME]})

def members_register(request):
    if request.method == 'POST':
        print "dddd"
        form = RegisterForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            try:
                Members.objects.using('default').create(member_card_id = str(info['member_card_id']),member_name = str(info['member_name']),\
                  members_id = str(info['member_id']),member_rank = str(info['member_rank']),member_phone=info['member_phone'],member_status=info['member_status'],\
                  member_create_time = info['member_createtime'],member_surplus=info['member_surplus'],member_points=info['member_points'],\
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
            Members.objects.using('default').get(id = to_del_list[i]).delete()
        except Exception,ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
    return HttpResponseRedirect('/members/')

def members_edit(request):
    if request.method == 'POST':
        member_card_id = request.POST.get('member_card_id', '')
        member_name = request.POST.get('member_name', '')
        member_password = request.POST.get('member_password2', '')
        member_sex = request.POST.get('member_sex','')
        members_id = request.POST.get('members_id','')
        member_phone = request.POST.get('member_phone','')
        member_rank = request.POST.get('member_rank', '')
        member_status = request.POST.get('member_status', '')
        member_createtime = request.POST.get('member_createtime', '') 
        member_points =request.POST.get('member_points', '')
        member_surplus = request.POST.get('member_surplus', '')
        try:
            Members.objects.using('default').filter(member_card_id = member_card_id).update(member_name = member_name, member_password = member_password, member_sex = member_sex, members_id = members_id, member_phone = member_phone, member_rank = member_rank, member_status = member_status, member_create_time = member_createtime, member_points = member_points, member_surplus = member_surplus)
        except Exception,ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
        return HttpResponseRedirect('/members/')
    else:
        edit_item = request.GET.get('cb', '')
        try:
            member  = Members.objects.using('default').get(id = edit_item)
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
                   results = Members.objects.using('default').filter(member_card_id__contains=card_id, member_name__contains=mem_name, member_rank__contains=mem_rank)
               else:
                   results = Members.objects.using('default').filter(member_card_id__contains=card_id, member_rank__contains=mem_rank)
           else:
               if mem_name != '':
                   results = Members.objects.using('default').filter(member_card_id__contains=card_id, member_name__contains=mem_name)
               else:
                   results = Members.objects.using('default').filter(member_card_id__contains=card_id)                   
       else:
           if mem_rank != 'all':
               if mem_name != '':
                   results = Members.objects.using('default').filter(member_name__contains=mem_name, member_rank__contains=mem_rank)
               else:
                   results = Members.objects.using('default').filter(member_rank__contains=mem_rank)
           else: 
               if mem_name != '':
                   results = Members.objects.using('default').filter(member_name__contains=mem_name)
               else:
                   results = Members.objects.using('default').all()
    return render_to_response('members_list.html',{'members':results, 'user':request.session[USERNAME]})

def rule(request):
    return render_to_response('rule.html',{'user':request.session[USERNAME]})

def member_rule(request):
    return render_to_response('mem_rule.html',{'user':request.session[USERNAME]})
    
def cards_list(request):
    members = Members.objects.using('default').all()
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
        n = Members.objects.using('default').get(member_card_id=member_card_id,member_name=member_name)
        count = float(rechange) + n.member_surplus
        Members.objects.using('default').filter(member_card_id=member_card_id,member_name=member_name).update(member_surplus=count)
        return HttpResponseRedirect('/cards/')
    else:
        edit_item = request.GET.get('cb', '')
        try:
            member  = Members.objects.using('default').get(id = edit_item)
        except Exception, ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
    return render_to_response('rechange.html',{'member':member,'user':request.session[USERNAME]})
    
def cards_loss(request):
    if request.method == 'POST': 
        member_card_id = request.POST.get('member_card_id', '')
        member_name = request.POST.get('member_name', '')
        status = request.POST.get('status','')
        if status == '':
            return HttpResponseRedirect('/cards/')
        Members.objects.using('default').filter(member_card_id=member_card_id,member_name=member_name).update(member_status=status)
        return HttpResponseRedirect('/cards/')
    else:
        edit_item = request.GET.get('cb', '')
        try:
            member  = Members.objects.using('default').get(id = edit_item)
        except Exception, ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
    return render_to_response('cards_loss.html',{'member':member,'user':request.session[USERNAME]})
    
def cards_search(request):
    if request.method == 'POST':
       card_id = request.POST.get('list_search')
       mem_status = request.POST.get('mem_status')
       mem_name = request.POST.get('mem_name')
       print mem_name, mem_status, card_id
       if smart_str(card_id) !='会员卡号':
           if mem_status != 'all':
               if mem_name != '':
                   results = Members.objects.using('default').filter(member_card_id__contains=card_id, member_name__contains=mem_name, member_status__contains=mem_rank)
               else:
                   results = Members.objects.using('default').filter(member_card_id__contains=card_id, member_status__contains=mem_status)
           else:
               if mem_name != '':
                   results = Members.objects.using('default').filter(member_card_id__contains=card_id, member_name__contains=mem_name)
               else:
                   results = Members.objects.using('default').filter(member_card_id__contains=card_id)                   
       else:
           if mem_status != 'all':
               if mem_name != '':
                   results = Members.objects.using('default').filter(member_name__contains=mem_name, member_status__contains=mem_status)
               else:
                   results = Members.objects.using('default').filter(member_status__contains=mem_status)
           else: 
               if mem_name != '':
                   results = Members.objects.using('default').filter(member_name__contains=mem_name)
               else:
                   results = Members.objects.using('default').all()
    for i in results:
            i.member_status = a[int(i.member_status) - 1]
    return render_to_response('members_cards.html',{'members':results, 'user':request.session[USERNAME]})

def cards_consume(request):
    if request.method == 'POST':
        form = ConsumerForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            card = info[str('card')]
            try:
                result = Members.objects.using('default').get(member_card_id=card)
            except Exception,ex:
                return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
            money = info[str('money')]
            method = info[str('method')]
            if result.member_status == '1':
                result.member_status = a[int(result.member_status) - 1]   
                if int(method) == 0:
                    if result.member_surplus < float(money):
                        error_m = '卡内余额不足 !'
                        return render_to_response('error.html',{'error':error_m,'user':request.session[USERNAME]})
                    else:
                        result.member_surplus  -= float(money)
                        result.member_points += float(money)
                        Members.objects.using('default').filter(member_card_id=card).update(member_surplus = result.member_surplus, member_points = result.member_points)
                else:
                    result.member_points += float(money)
                    Members.objects.using('default').filter(member_card_id=card).update(member_points = result.member_points)
                return HttpResponseRedirect('/cards/')
            error_m = '该会员卡处于非正常状态 !'
            return render_to_response('error.html',{'error':error_m,'user':request.session[USERNAME]})
    else:
        form = ConsumerForm()
    return render_to_response('cards_consume.html',{'forms':form,'user':request.session[USERNAME]})
