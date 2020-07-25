"""harsh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from first import views
from django.urls import path
#from dajaxice.core import dajaxice_autodiscover, dajaxice_config

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url('login/',views.login, name='login'),
    url('register/', views.reg, name='register'),
    url('logout/', views.logout, name='logout'),
    path('<str:username>/', views.show,name="show"),
    path('<str:username>/ask/', views.ask,name="show"),
    path('ans/<str:ques_id>/', views.ans,name="ans"),
    path('user/delete/<str:ques_id>/', views.dlt,name="dlt"),
    url('user/profile/', views.profile, name='profile'),
    url('user/image1/', views.image1, name='image1'),
    url('user/image2/', views.image2, name='image2'),
    url('user/image3/', views.image3, name='image3'),
    url('user/image4/', views.image4, name='image4'),
#    url(r'^user/create/$', views.submit),
#    url(r'^favicon.ico/$', views.s),
    url('admin/', admin.site.urls),
]

handler500 = views.handler500
