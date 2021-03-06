from django.conf.urls import patterns, include, url
from django.contrib import admin

from morado import views as morado_views

urlpatterns = patterns('',

    url(r'^$', morado_views.HomeView.as_view(), name='home'),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
)
