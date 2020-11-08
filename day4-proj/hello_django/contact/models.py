from django.db import models

# Create your models here.

# 定义Contact类，且继承models.Model类


class Contact(models.Model):
    # 定模型含有属性，及相应属性值长度
    name = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=11)
    password = models.CharField(max_length=400)
