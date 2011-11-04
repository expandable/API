# -*- coding: utf-8 -*-
from django.db import models
from clubs.models import Club

# Create your models here.
class AbstractGroup(models.Model):
    label = models.CharField(max_length=8)

    class Meta:
        abstract = True

class ClassGroup(AbstractGroup):
    pass

class SecondLanguageGroup(AbstractGroup):
    pass

class ThirdLanguageGroup(AbstractGroup):
    pass

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.SlugField(max_length=8, unique=True)
    birthdate = models.DateField(blank=True)
    photo = models.ImageField(upload_to='photos', max_length=8, blank=True)
    email = models.EmailField(unique=True)
    salt = models.CharField(max_length=10)
    password = models.CharField(max_length=40)
    leaving_year = models.IntegerField()
    class_group = models.ForeignKey(ClassGroup, related_name='users')
    second_group = models.ForeignKey(SecondLanguageGroup, null=True, related_name='users')
    third_group = models.ForeignKey(ThirdLanguageGroup, null=True, related_name='users')
    phone_number = models.CharField(max_length=10, blank=True)
    nickname = models.CharField(max_length=20, blank=True)
    clubs = models.ManyToManyField(Club, related_name='users')
