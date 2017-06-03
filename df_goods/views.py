#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import *
# Create your views here.
def index(request):
    t1_click= GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[0:3]
    t1_new=GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[0:4]
    t3_click = GoodsInfo.objects.filter(gtype_id=3).order_by('-gclick')[0:3]
    t3_new=GoodsInfo.objects.filter(gtype_id=3).order_by('-id')[0:4]
    t4_click = GoodsInfo.objects.filter(gtype_id=4).order_by('-gclick')[0:3]
    t4_new=GoodsInfo.objects.filter(gtype_id=4).order_by('-id')[0:4]
    t5_click = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[0:3]
    t5_click = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[0:3]
    t6_new=GoodsInfo.objects.filter(gtype_id=6).order_by('-id')[0:4]
    t6_new=GoodsInfo.objects.filter(gtype_id=6).order_by('-id')[0:4]
    context={'title':'首页',
             't1_click':t1_click,'t1_new':t1_new,
             't3_click':t3_click,'t3_new':t3_new,
             't4_click': t3_click, 't4_new': t3_new,
             't5_click': t3_click, 't5_new': t3_new,
             't6_click': t3_click, 't6_new': t3_new,
             }
    return render(request,'df_goods/index.html',context)

def index2(request,tid):
    #查询点击最高、最新的商品
    t1_click= GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')[0:3]
    t1_new=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')[0:4]
    #构造点击量最高的商品列表
    click_list=[]
    for click in t1_click:
        click_list.append({'id':click.id,'title':click.gtitle})
    #构造最新的商品列表
    new_list=[]
    for new in t1_new:
        new_list.append({'id':new.id,'title':new.gtitle,'price':new.gprice,'pic':new.gpic.name})
    #返回json
    context={'click_list':click_list,'new_list':new_list}
    return JsonResponse(context)

def list(request):
    pass

def detail(request):
    pass
