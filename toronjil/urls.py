from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'morado.views.HomeView.as_view()', name='home'),
    # url(r'^/tasklist$', 'morado.views.tasklist', name='tasklist'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
