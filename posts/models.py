

from django.db import models
from django.db.models.base import Model
from django.db.models.manager import BaseManager
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
#import misaka
# Create your models here.
from groups.models import Group, GroupMember
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
User=get_user_model()

class Post(models.Model):
    id =models.AutoField(primary_key=True)
    user=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at= models.DateTimeField( auto_now=True)
    question=RichTextField(blank=True,null=True)
    #question=models.TextField()
    question_html=RichTextField(editable=False)
    group =models.ForeignKey(Group,related_name='posts',null=True,blank=False,on_delete=models.CASCADE,
    #limit_choices_to={'name__in': User.pk}
    )
    video=models.FileField(upload_to="video/%y",null=True,blank=True)
    image=models.FileField(null=True,blank=True)

    #caption=models.CharField(max_length=250,null=True,blank=True)
     
    
    def save(self,*args,**kwargs):
        self.question_html=self.question
        super().save(*args,**kwargs)


    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"pk": self.pk,'username':self.user.username})
    
    def approved_comments(self):
        return self.comments.filter(approved_comments=True)


    
    class Meta:
        ordering=['-created_at']
    def __str__(self):
        return self.question
    
    
class Comment(models.Model):
    id =models.AutoField(primary_key=True)
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    text=RichTextField(blank=True,null=True)
    created_date =models.DateTimeField(auto_now=True)
    approved_comment=models.BooleanField(default=False)
    likes=models.ManyToManyField(User,related_name='like_posts')    
    like=models.BooleanField(default=True)   
    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse('posts:all')

    def total_likes(self):
        return self.likes.count()
    
    def likeif(self):
        if self.like ==True :
            return True
        else:
            return False
    
    
    def __str__(self):
        return self.text



