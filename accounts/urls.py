from django.urls import include, re_path ,path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from django.shortcuts import HttpResponseRedirect



app_name = 'accounts'
urlpatterns = [
    re_path(r'^$',views.home , name = 'home'),
    re_path(r'^login/$' ,LoginView.as_view(template_name = 'login.html' ) ),
    re_path(r'^logout$' ,LogoutView.as_view()),
    re_path(r'^signup$',views.register , name = 'register'),
    re_path (r'^(?P<slug>[-\w]+)/$',views.profile , name = 'profile'),
    re_path (r'^(?P<slug>[-\w]+)/edit$',views.edit_profile , name = 'profile_edit'),

]
