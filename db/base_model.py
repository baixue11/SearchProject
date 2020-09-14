from django.db import models


class BaseModel(models.Model):
    '''模型抽象基类'''
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        # 说明是一个抽象模型类
        abstract = True