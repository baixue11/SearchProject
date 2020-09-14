# -*- coding: utf-8 -*-
from django.db import models
from db.base_model import BaseModel
# Create your models here.

class ProductInfo(BaseModel):
    '''商品表'''

    name = models.CharField(max_length=20, verbose_name='名称')
    desc = models.CharField(max_length=256, verbose_name='描述')

    class Meta:
        db_table = 'product_info'
        verbose_name = "商品表"
        verbose_name_plural = verbose_name