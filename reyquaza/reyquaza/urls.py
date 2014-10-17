from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reyquaza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)


urlpatterns += patterns('suicune.views',
                        )
urlpatterns += patterns('entei.views',
                        url(r'^$', 'index', name='index'),
                        url(r'^search/(?P<extension_name>\S+)/$', 'search_extension', name='search_extension'),

                        )
urlpatterns += staticfiles_urlpatterns()