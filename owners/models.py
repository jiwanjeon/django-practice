from pydoc import describe
from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age = models.IntegerField(default=0)

    class Meta:
        db_table = 'owners'

class Dog(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField(default=0)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, related_name='dogs')

    # related_name은 뭘까??
    # https://fabl1106.github.io/django/2019/05/27/Django-26.-%EC%9E%A5%EA%B3%A0-related_name-%EC%84%A4%EC%A0%95%EB%B0%A9%EB%B2%95.html

    class Meta: 
        db_table = 'dogs'