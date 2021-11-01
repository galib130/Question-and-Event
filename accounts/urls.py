from django.conf.urls import url
from django.contrib.auth import views as auth_views #contains default view for login and logout


from . import views

app_name ='accounts' #app name for url


urlpatterns = [
    url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'), #url for login
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),#url for logout
    url(r'signup/$',views.Signup.as_view(),name='signup')#url for signup

]
