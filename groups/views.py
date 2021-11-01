from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.contrib import messages
# Create your views here.

from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views import generic
from groups.models import Group,GroupMember
from django.shortcuts import get_object_or_404
from . import models

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields=('name','description')
    model =Group


    def form_valid(self,form):
        self.object= form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        
        
        return super().form_valid(form)

class SingleGroup(generic.DetailView):
    model=Group

class ListGroups(generic.ListView):
    model=Group


class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        group=get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        
        except :
            messages.warning(self.request,'Warning already a member!')
        else:
            messages.success(self.request,'You are henceforth a member')
            
        return super().get(request,*args,**kwargs)


class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    def get(self,request,*args,**kwargs):
        try:
            membership= models.GroupMember.objects.filter(
            user=self.request.user,
            group__slug=self.kwargs.get('slug') ).get() 

        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry you are not in this group!')

        else:
            membership.delete()
            messages.success(self.request,'You left the group!') 

        return super().get(request,*args,**kwargs)


class DeleteGroup(LoginRequiredMixin,generic.DeleteView):
    model=models.Group
    select_related=('user','group')
    success_url=reverse_lazy('home')
    def  get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Group Deleted')
        return super().delete(*args,**kwargs)

    



