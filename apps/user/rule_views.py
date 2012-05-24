#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils.encoding import smart_str, smart_unicode
import StringIO
from PIL import Image

import time
import datetime
from apps.models.members import Members
from apps.models.rule import *
from apps.auth.static import *


a = ['正常', '锁定','挂失']
def rank_set(request):
    if request.method == 'POST':
        rankA = request.POST.get('rankA')
        rankB = request.POST.get('rankB')
        rankC = request.POST.get('rankC')

        print rankA, rankB, rankC, '======================'
        if rankA == '' or rankB == '' or rankC == '':
            error_m = '不能为空 !'
            return render_to_response('rule.html',{'error':error_m,'user':request.session[USERNAME]})
        if int(rankA) > int(rankB) or int(rankB) > int(rankC):
            error_m = '要求:普卡 ≤ 银卡≤ 金 (元)'
            return render_to_response('rule.html',{'error':error_m,'user':request.session[USERNAME]})
        try:
            Rank.objects.using('default').filter(id = 1).update(ranka = int(rankA),rankb = int(rankB), rankc = int(rankC))
        except Exception,ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
        return HttpResponseRedirect('/index')
    else:
        rank = Rank.objects.using('default').get(id = 1)
    return render_to_response('rank_rule.html',{'rank':rank,'user':request.session[USERNAME]})
        
def proportion(request):
    proportionals = Proportional.objects.using('rule').all()
    return render_to_response('points_rule.html',{'proportionals':proportionals,'user':request.session[USERNAME]}) 

def proportion_add(request):
    if request.method == 'POST':
        goods_type = request.POST.get('type')
        proportion = request.POST.get('proprotion')
        extra = request.POST.get('extra')

        if goods_type == '' or proportion == '' or extra == '':
           error_m = '不能为空!'
           return render_to_response('proportion_add.html',{'error':error_m,'user':request.session[USERNAME]}) 
        tmp = proportion.split("/")
        if len(tmp) != 2 or not tmp[0].isdigit() or not tmp[1].isdigit():
            error_m = '格式错误!'
            return render_to_response('proportion_add.html',{'error_m':error_m,'user':request.session[USERNAME]})
        try:
            Proportional.objects.using('rule').create(goodstype = goods_type, proportion = proportion, extra = extra)
        except Exception,ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
        return HttpResponseRedirect('/rule') 
    return render_to_response('proportion_add.html',{'user':request.session[USERNAME]})

def proportion_delete(request):
    to_del_list = request.GET.getlist('cb')
    num = len(to_del_list)
    for i in range(num):
        try:
            Proportional.objects.using('rule').get(id = to_del_list[i]).delete()
        except Exception,ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
    return HttpResponseRedirect('/rule/')

def proportion_edit(request):
    if request.method == 'POST':
        proportion_id = request.POST.get('id')
        goods_type = request.POST.get('type')
        proportion = request.POST.get('proprotion')
        extra = request.POST.get('extra')

        if goods_type == '' or proportion == '' or extra == '':
            error_m = '不能为空!'
            return render_to_response('proportion_add.html',{'error':error_m,'user':request.session[USERNAME]})
        tmp = proportion.split("/")
        if len(tmp) != 2 or not tmp[0].isdigit() or not tmp[1].isdigit():
             error_m = '格式错误!'
             return render_to_response('proportion_add.html',{'error_m':error_m,'user':request.session[USERNAME]})
        try:
             Proportional.objects.using('rule').filter(id = proportion_id).update(goodstype = goods_type, proportion = proportion, extra = extra)
        except Exception,ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
        return HttpResponseRedirect('/rule')
    else:
        edit_item = request.GET.get('cb', '')
        proportions = Proportional.objects.using('rule').get(id = edit_item)
    return render_to_response('proportion_edit.html',{'proportions':proportions,'user':request.session[USERNAME]})

def gift_list(request):
    gifts_rankA = Gift.objects.using('rule').filter(rank = "A").order_by("id")
    for i in gifts_rankA:
        i.name = i.name.split('|')

    gifts_rankB = Gift.objects.using('rule').filter(rank = "B").order_by("id")
    for i in gifts_rankB:
            i.name = i.name.split('|')

    gifts_rankC = Gift.objects.using('rule').filter(rank = "C").order_by("id")
    for i in gifts_rankC:
            i.name = i.name.split('|')

    return render_to_response('gift_list.html',{'gifts_rankA':gifts_rankA, 'gifts_rankB':gifts_rankB,'gifts_rankC':gifts_rankC,'user':request.session[USERNAME]})

def gift_add(request):
    if request.method == 'POST':
        buf = request.FILES.get('photo', None) 
        gift_name = request.POST.get('name')
        gift_price = request.POST.get('price')
        gift_points = request.POST.get('points')
        gift_rank = request.POST.get('rank')

        #upload photo
        try:
            data = buf.read()
            f = StringIO.StringIO(data)
            image = Image.open(f)
            image = image.convert('RGB')
            name = '%s%s' % (UPLOAD_URL, buf.name)
            image.save(file(name, 'wb'), 'PNG')
        except Exception,ex:
            error_m = '无法打开图片'
            return render_to_response('gift_add.html',{'error':ex,'user':request.session[USERNAME]})
 
        gift_name = "|".join([gift_name,name])
        # mysql
        Gift.objects.using('rule').create(name = gift_name, price = gift_price, points=gift_points,rank = gift_rank)
        return HttpResponseRedirect('/gift')
    else:
        return render_to_response('gift_add.html',{'user':request.session[USERNAME]})

def gift_delete(request):
    to_del_list = request.GET.getlist('cb')
    num = len(to_del_list)
    for i in range(num):
        try:
            Gift.objects.using('rule').get(id = to_del_list[i]).delete()
        except Exception,ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
    return HttpResponseRedirect('/gift/')

def gift_edit(request):
    if request.method == 'POST':
        gift_id = request.POST.get('id')
        gift_name = request.POST.get('name')
        price = request.POST.get('price')
        points = request.POST.get('points')
        rank = request.POST.get('rank')

        gift = Gift.objects.using('rule').get(id = gift_id)
        l = gift.name.split("|")
        l[0] = gift_name
        name = "|".join(l)
        gift.name = name
        gift.price = price
        gift.points = points
        gift.rank = rank
        gift.save()
#        Gift.objects.using('rule').filter(id = gift_id).update(name = name, price = price, points = points, rank = rank)
        return HttpResponseRedirect('/gift/')
    else:   
        edit_item = request.GET.get('cb', '')
        gift  = Gift.objects.using('rule').get(id = edit_item)
        gift.name = gift.name.split('|')
    return render_to_response('gift_edit.html',{'gift':gift,'user':request.session[USERNAME]})

def cards_ss(request):
    if request.method == 'POST':
        card = request.POST.get('cardid')
        try:
            result = Members.objects.using('users').get(member_card_id = card)
        except Exception,ex:
            error_m = "该会员不存在 !"
            return render_to_response('point_gift.html',{'error':error_m,'user':request.session[USERNAME]})
    #print type(str(result.member_end_time)), type(str(time.strftime("%Y-%m-%d",time.localtime())))
    #print str(result.member_end_time) < str(time.strftime("%Y-%m-%d",time.localtime()))
        result_lists = Gift.objects.using('rule').all()
        result_list = []
        for i in result_lists:
            print result.member_rank, i.rank
            if result.member_rank >= i.rank: 
                if int(i.points) <= int(result.member_points):
                    result_list.append(i)
        #判断是否过期 
        if str(result.member_end_time) < time.strftime("%Y-%m-%d",time.localtime()):
            error_m = '该会员已过期,请续期!'
            Members.objects.using('users').filter(member_card_id=card).update(member_status = '1')
            return render_to_response('point_gift.html',{'error':error_m,'member':result,'user':request.session[USERNAME]})
        for i in result_list:
            i.name = i.name.split('|')[0]

        result.member_status = a[int(result.member_status) - 1]
        return render_to_response('point_gift.html',{'gifts':result_list,'member':result,'user':request.session[USERNAME]})
    return render_to_response('point_gift.html',{'user':request.session[USERNAME]})
    
def point_gift(request):
    if request.method == 'POST':
        gift = request.POST.get('gift_list') 
        mem_name = request.POST.get('name')
        mem_points = request.POST.get('points')
        if mem_name == '':
            error_m = '请输入会员卡号 !'
            return render_to_response('point_gift.html',{'error':error_m,'user':request.session[USERNAME]})
        if gift == None:
            error_m = '积分不足不能兑换商品!'
            return render_to_response('point_gift.html',{'error':error_m,'user':request.session[USERNAME]})
        member = Members.objects.using('users').get(member_name = mem_name, member_points = mem_points)
        result = Gift.objects.using('rule').get(name__contains = gift)    
        member.member_points = member.member_points - int(result.points)
        member.save()
        return HttpResponseRedirect('/gift/')
    return render_to_response('point_gift.html',{'user':request.session[USERNAME]})
