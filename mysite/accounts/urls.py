from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from accounts import views 
 
app_name = 'accounts'
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mypage/$', views.mypage, name='mypage'),
    url(r'^redilect/$', views.redilect, name='redilect'),
    url(
        r'^login/$',
        auth_views.LoginView.as_view(
            template_name='accounts/login.html'
        ),
        name='login'
    ),
    url(
        r'^logout/$',
        auth_views.LogoutView.as_view(
            template_name='accounts/logout.html'
        ),
        name='logout'
    ),
]