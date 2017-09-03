from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^save/$', views.save, name='save'),	
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'gameapp/login.html'}, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'gameapp/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^accounts/profile/$', views.home, name='home'),
    url(r'^playgame/$', views.gamepage, name='gamepage'),
    url(r'^scorecard/$', views.scorecard, name='scorecard'),
    url(r'^$', views.home, name='home'),

]

