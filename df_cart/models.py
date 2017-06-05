# coding=utf-8
from django.db import models
from df_goods.models import *
from df_user.models import *
# Create your models here.


class CartInfo(models.Model):
    # 购买数量
    count = models.IntegerField()
    # 用户
    user = models.ForeignKey(UserInfo)
    # 购买的商品信息
    goods = models.ForeignKey(GoodsInfo)
