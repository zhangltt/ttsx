#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import *
from django.core.paginator import Paginator,Page
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


def list(request,tid,index,sort):
    # 获取tid获取分类

    typeinfo = TypeInfo.objects.get(pk=int(tid))
    #print typeinfo
    # 获取最新推荐的两件商品,通过id降序
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
   # print news[0].gtitle
    # 根据默认(新品) 1,价格 2,人气排序 3

    if sort == '1':
        goods_list = typeinfo.goodsinfo_set.order_by('-id')
        #goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort == '2':
        goods_list = typeinfo.goodsinfo_set.order_by('-gprice')
        #goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    elif sort == '3':
        goods_list = typeinfo.goodsinfo_set.order_by('-gclick')
        #goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')

    # 创建Paginator对象,每页显示10个
    paginator = Paginator(goods_list, 10)
    # 获取page对象,显示第index页的数据
    pages = paginator.page(int(index))
    print pages.number
    #print goods_list[0].gtitle
    #print good1_list[0].gtitle
    context={'pages':pages,'new':news,
             'sort':sort,
             'paginator':paginator,
             'typeinfo':typeinfo,
             }
    #return JsonResponse(context)
    return render(request,'df_goods/list.html',context)

def detail(request,tid):
    # 通过商品id找到商品对象
    goodinfo = GoodsInfo.objects.get(pk=tid)
    # 获取分类两件新品
    news = goodinfo.gtype.goodsinfo_set.order_by('-id')[0:2]
    # 加点击量
    goodinfo.gclick = goodinfo.gclick+1
    goodinfo.save()

    print news



    context = {'title':'天天生鲜商品详情',
               'goodinfo':goodinfo,
               'news':news
               }
    return render(request,'df_goods/detail.html',context)

# 自定义搜索视图类
from haystack.views import SearchView
class MySearchView(SearchView):
    def extra_context(self):
        extra = super(MySearchView, self).extra_context()

        # title为网页标题部分显示的文字变量名,其他的都是固定值
        extra['title']=self.request.GET.get('q')

        return extra