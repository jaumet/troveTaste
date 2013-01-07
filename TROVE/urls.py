from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TROVE.views.home', name='home'),
    # url(r'^TROVE/', include('TROVE.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    ##url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    ##url(r'^admin/', include(admin.site.urls)),

    # Home
    url(r'^$', 'trove_txt.views.index'),

    # testing
    url(r'^test$|^test/$', 'trove_txt.views.test'),

    # testing
    url(r'^cercle$|^cercle/$', 'trove_txt.views.cercle'),

    # Getting the results
    url(r'^get$|^get/$', 'trove_txt.views.get'),

    # JSON responses:
    ## APACHE wsgi: 
    url(r'^test/(?P<query>.*)/$', 'trove_txt.views.trove_query'),

    ## Comparation data from ddbb
    url(r'^comparing/(?P<query>.*)/$', 'trove_txt.views.comparing'),

    # about page
    url(r'^about$|^about/$', 'trove_txt.views.about')

)
