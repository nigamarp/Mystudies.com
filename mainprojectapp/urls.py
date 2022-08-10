from django import views
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('login_data',views.login_data,name='login_data'),
    path('signup_data',views.signup_data,name='signup_data'),
    path('comment_save',views.comment_save,name='comment_save'),
    path('logout',views.logout,name='logout'),
    path('course',views.course,name='course'),
    path('know_more',views.know_more,name='know_more'),
    path('blog',views.blog,name="blog"),
    path('blog1',views.blog1,name="blog1"),
    path('blog2',views.blog2,name="blog2"),
    path('blog3',views.blog3,name="blog3"),
    path('blog4',views.blog4,name="blog4"),
    path('blog5',views.blog5,name="blog5"),
    path('blog6',views.blog6,name="blog6"),
    path('blog7',views.blog7,name="blog7"),
    path('blog8',views.blog8,name="blog8"),
    path('blog9',views.blog9,name="blog9"),
    path('blog10',views.blog10,name="blog10"),
    path('blog11',views.blog11,name="blog11"),
]
