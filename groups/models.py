from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.db import IntegrityError
from django.http import HttpResponseRedirect, request
from django.contrib import messages
from django.shortcuts import render


# Create your models here.

#import misaka

from django.contrib.auth import get_user_model

User = get_user_model()

from django import template
register =template.Library()

class Group(models.Model): #create model for selecting groups
    id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=225,unique=True)
    slug= models.SlugField(allow_unicode=True,unique=True)
    description= models.TextField(blank=True,default='')
    description_html=models.TextField(editable=False,default='',blank=True)
    members=models.ManyToManyField(User,through='GroupMember',blank=True)
    user=models.ForeignKey(User,related_name='group_owner',on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name+self.description)
        #self.description_html=misaka.html(self.description)
        self.description_html=self.description
        super().save(*args,**kwargs)
      


 

    def get_absolute_url(self):
        return reverse ('groups:single',kwargs={'slug':self.slug})
    
    class Meta:
        ordering=['name']


class GroupMember(models.Model):
    id =models.AutoField(primary_key=True)
    group =models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user =models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.user.username

    class Meta:
        unique_together =('group','user')
        
