#coding=utf8
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

from django.shortcuts import render
from django.http import JsonResponse
from df_user.user_decorator import *
from models import *
from df_user.models import *
# Create your views here.


@login
def cart(request):
    # 获取登陆用户购物车中商品的对象
    goodscart = CartInfo.objects.filter(user_id=request.session['user_id'])
    print '======'
    print goodscart[0].count

    context = {'page_name':1,
               'title':'购物车',
               'name':'购物车',
               'goodscart':goodscart,
               }
    return render(request,'df_cart/cart.html',context)
@login
def add(request,gid,count):
    # {'nameaa':name,'nums':nums,'delet':delet}

    result = request.GET
    glist = result.get('glist')

    print glist,'glist'
    if  glist == 'ok':
        goodid = result.get('goodid')
        count = result.get('count')

        print '1-----'
        print CartInfo.objects.filter(id=int(goodid))
        print goodid
        carts = CartInfo.objects.filter(id=int(goodid)).filter(user_id=request.session['user_id'])
        print carts,'carts'

        if len(carts) == 0:

            cart = CartInfo()
            cart.count = int(count)
            cart.user_id = request.session['user_id']
            cart.goods_id = int(gid)
            cart.save()
            # 如果不为0 取出列表中的模型类对象增加商品的数量
        else:
            cart = carts[0]
            cart.count += int(count)
            cart.save()

            return JsonResponse({'result':cart.count})



        print carts,'carts'
        print goodid ,'goodis'
        print count, 'count'
        return JsonResponse({'result':cart.count})

    else:
        # 通过gid和session中的user_id查询商品
        print request.session['user_id'],'用户id'
        #print CartInfo.objects.filter(goods_id=gid)

        carts = CartInfo.objects.filter(goods_id=gid).filter(user_id=request.session['user_id'])
        #print carts,11
        # 判断返回列表的长度如果为0创建一个模型类的对象添加商品id 用户名 数量
        if len(carts) == 0:

            cart = CartInfo()
            cart.count = int(count)
            cart.user_id =request.session['user_id']
            cart.goods_id=int(gid)
            cart.save()
        # 如果不为0 取出列表中的模型类对象增加商品的数量
        else:
            cart = carts[0]
            cart.count+=int(count)
            cart.save()
        #判断如果是ajax请求返回JsonResponse对象 key为数量(购物车上的数字)
        print carts,1



    if request.is_ajax():
        print carts
        return JsonResponse({'a':cart.count})

def delete(request):
    id = request.GET.get('goodid')
    cart = CartInfo.objects.get(id=int(id))
    cart.delete()
    return JsonResponse({'result': 'ok'})

@login
def place(request):
    # 获取用户地址
    user = UserInfo.objects.filter(pk=request.session['user_id'])
    print user
    if len(user)>0:
        print '----'
        addres = user[0].uaddress
        youbian = user[0].uyoubian
        phone = user[0].uphone
        name = user[0].uname
        usersrt = '%s 邮编%s 姓名:%s 联系方式:%s'%(addres,youbian,name,phone)
        print usersrt
    result = request.POST
    cartids = result.getlist('cartid')
    print cartids,'cartid'
    cart_list = []
    for i in cartids:
        cart = CartInfo.objects.filter(pk=i)
        cart_list.append(cart[0])
    print cart_list
    print cart

    # 获取提交商品




    context = {'page_name': 1,
               'title': '提交订单',
               'name':'提交订单',
                'addr':usersrt,
               'cartids':cart_list,
               }

    return render(request,'df_cart/placeOrder.html',context)