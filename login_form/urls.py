from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'login_form.views.home', name='home'),
    # url(r'^login_form/', include('login_form.foo.urls')),
    url(r'^$', 'login_system.views.index'),
    url(r'users/add', 'login_system.views.add'),
    url(r'users/login', 'login_system.views.login'),
    url(r'TESTAPI/resetFixture', 'login_system.views.TESTAPI_resetFixture'),
    url(r'TESTAPI/unitTests', 'login_system.views.TESTAPI_unitTests'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
