from django.conf.urls import url


from . import views



app_name='accounts'


urlpatterns=[

    url(r'^login/', views.UserLoginView.as_view(), name='login'),
    url(r'^logout/',views.UserLogoutView.as_view(), name='logout'),
    url(r'^signup/', views.UserCreateView.as_view(), name ='signup'),
    url(r'^edit/(?P<pk>\d+)/$', views.UserEditView.as_view(), name ='edit'),

]