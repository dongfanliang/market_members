#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils.encoding import smart_str, smart_unicode
import StringIO
from PIL import Image

from apps.models.rule import *
from apps.auth.static import *


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
             #Proportional.objects.using('rule').filter(id = )
             pass
        except Exception,ex:
            return render_to_response('error.html',{'error':ex,'user':request.session[USERNAME]})
        return HttpResponseRedirect('/rule')
    else:
        edit_item = request.GET.get('cb', '')
        proportions = Proportional.objects.using('rule').get(id = edit_item)
    return render_to_response('proportion_edit.html',{'proportions':proportions,'user':request.session[USERNAME]})

def gift_list(request):
    gifts_rankA = Gift.objects.using('rule').filter(rank = "普通会员所有").order_by("id")
    for i in gifts_rankA:
        i.name = i.name.split('|')

    gifts_rankB = Gift.objects.using('rule').filter(rank = "仅银卡以上会员所有").order_by("id")
    for i in gifts_rankB:
            i.name = i.name.split('|')

    gifts_rankC = Gift.objects.using('rule').filter(rank = "仅金卡会员所有").order_by("id")
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
        Gift.objects.using('rule').filter(id = gift_id).update(name = name, price = price, points = points, rank = rank)
        return HttpResponseRedirect('/gift/')
    else:   
        edit_item = request.GET.get('cb', '')
        gift  = Gift.objects.using('rule').get(id = edit_item)
        gift.name = gift.name.split('|')
    return render_to_response('gift_edit.html',{'gift':gift,'user':request.session[USERNAME]})


