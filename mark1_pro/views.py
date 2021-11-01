from django.views.generic import TemplateView
from django.shortcuts import render,HttpResponse
from posts.models import Post,Comment,User
from groups.models import Group
class HomePage(TemplateView):
    template_name='index.html'

class InPage(TemplateView):
    template_name='in.html'


class OutPage(TemplateView):
    template_name='out.html'



def search(request):
   query=request.GET['search'] 
   allPosts=Post.objects.filter(question__icontains=query)
   params={'allPosts':allPosts}
   return render(request,'search.html',params)

def search_group(request):
   query=request.GET['search_group'] 
   allGroups=Group.objects.filter(name__icontains=query)
   params={'allGroups':allGroups}
   return render(request,'search_group.html',params)

