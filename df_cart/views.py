#coding=utf8
from django.shortcuts import render
from django.http import JsonResponse
from df_user.user_decorator import *
from models import *
from df_user.models import *
# Create your views here.


@login
def cart(request):
    page_name = 1
    context = {'page_name':page_name}
    return render(request,'df_cart/cart.html',context)
@login
def add(request,gid,count):
    # 通过gid和session中的user_id查询商品
    #print gid
    #print CartInfo.objects.filter(goods_id=gid)

    carts = CartInfo.objects.filter(goods_id=gid).filter(user_id=request.session['user_id'])
   # print carts,11
    # 判断返回列表的长度如果为0创建一个模型类的对象添加商品id 用户名 数量
    if len(carts) == 0:
        cart = CartInfo()
        cart.count = int(count)
        cart.user_id =cart.user.id
        cart.goods_id=int(gid)
        #print cart.user_id
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
    # 否则返回购物车列表页(点击我的购物车部分)



        #return JsonResponse({'a':1})