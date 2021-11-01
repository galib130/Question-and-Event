from django.conf.urls import url

from . import views


app_name='posts'

urlpatterns = [
    url(r'^$',views.PostList.as_view(),name='all'),
    url(r'^new/$',views.CreatePost.as_view(),name='create'),
    url(r'^by/(?P<username>[-\w]+)/$',views.UserPosts.as_view(),name='for_user'),
    url(r'^by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='single'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeletePost.as_view(),name='delete'),
    url(r'^by/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment'),
    
    url(r'^update/(?P<pk>\d+)/$',views.UpdatePost.as_view(),name='update'),
    
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^comment/(?P<pk>\d+)/like/$',views.LikePost,name='like'),
    url(r'^event/$',views.EventList.as_view(),name='event_all'),
    url(r'^lcc/$',views.LCCList.as_view(),name='lcc_all'),

    ]
    


