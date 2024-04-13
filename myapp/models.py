from typing import Any
from django.db import models

class Tracking(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    tracking = models.CharField(max_length=100,null=True,blank=True)
    other = models.TextField(null=True,blank=True)

    def __str__(self):
        return '{} - {} ({})'.format(self.name, self.tel, self.tracking)
    

class Officer(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    other = models.TextField(null=True,blank=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.tel)
    

class AskQA(models.Model):
    name = models.CharField(max_length=100, verbose_name='ชื่อผู้ติดต่อ')
    email = models.CharField(max_length=100,null=True,blank=True, verbose_name='อีเมล')
    title = models.CharField(max_length=100,null=True,blank=True, verbose_name='หัวข้อ')
    detail = models.TextField(null=True,blank=True, verbose_name='รายละเอียด')
    detail_answer = models.TextField(null=True,blank=True, verbose_name='คำตอบ')

    def __str__(self):
        return '{} - ({})'.format(self.name, self.title)


