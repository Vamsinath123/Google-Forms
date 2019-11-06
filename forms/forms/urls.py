from django.conf.urls import url, include
from django.contrib.auth import views
from forms.survey import views as survey_views


urlpatterns = [
    url(r'^$', survey_views.main, name='main'),
    url(r'^login/$', views.LoginView.as_view(),{'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', survey_views.signup, name='signup'),
    url(r'^home/$', survey_views.home, name='home'),
    url(r'^password/$', survey_views.password, name='password'),
]