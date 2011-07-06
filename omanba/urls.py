from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
<<<<<<< HEAD
    #url(r'^omanba_app$', 'omanba_app.views.index', name='home'),
    #url(r'^omanba/', include('omanba.foo.urls')),
=======
    #url(r'^$', 'omanba.views.home', name='home'),
    # url(r'^omanba/', include('omanba.foo.urls')),
>>>>>>> 4d5a6750f01f5e8d8c6bf79983c87bf40cb48df8

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^omanba_app/', include('omanba.omanba_app.urls')),
=======
<<<<<<< HEAD
    url(r'^omanba_app/', include('omanba.omanba_app.urls')),
=======
    url(r'^omanba/', include('omanba.omanba_app.urls')),
>>>>>>> 4d5a6750f01f5e8d8c6bf79983c87bf40cb48df8
>>>>>>> 290c017d9d034ae892d00f3fc8a557fa1730f9db
)
