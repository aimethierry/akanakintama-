"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app.views import HomeView, BlogView,  AboutView, BlogCreate, BlogDetail, BlogList, BlogEdit, BlogDelete
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(template_name="home.html")),
    url(r'blog/$', BlogView.as_view(template_name="blog.html")),
    url(r'contact/$', views.contact, name="contact"),

    # url(r'try/$', views.post, name="try"),


    url(r'about/$', AboutView.as_view(template_name="about.html")),
    url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^blog/create/$', BlogCreate.as_view(), name="create"),
     url(r'^blog/(?P<pk>\d+)/$', BlogDetail.as_view(), name='order_detail'),

    url(r'^dashboard/list/$', BlogList.as_view(template_name="Listblog.html")),
    url(r'^detail/(?P<pk>\d+)/$', BlogEdit.as_view(), name='order_detail'),
    url(r'^delete/(?P<pk>\d+)/$', BlogDelete.as_view(), name='order_detail'),

   

]

if  settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
