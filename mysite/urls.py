from django.conf.urls import patterns, include, url
from signup import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^signup', views.sign_up_user),
    url(r'^invite', views.send_invite),
    url(r'^admin/', include(admin.site.urls)),
)
