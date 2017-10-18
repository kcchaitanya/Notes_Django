from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import django.contrib.auth.views
from django.conf import settings
from django.contrib.auth.views import logout





urlpatterns = [
    url ( r'^note/list/$', views.note_list, name='note_list' ),
    url ( r'^login/note/list/$', views.note_list, name='note_list' ),

    url ( r'^note/new/$', views.note_new, name='note_new' ),
    url ( r'^note/view/(?P<pk>\d+)/$', views.note_detail, name='note_detail' ),
    url ( r'^note/(?P<pk>\d+)/edit/$', views.note_edit, name='note_edit' ),
    url ( r'^note/delete/(?P<pk>\d+)/$', views.note_delete, name='note_delete' ),
    url ( r'^$', views.signup, name='signup' ),
    url(r'^login/$', django.contrib.auth.views.login, name='login'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]