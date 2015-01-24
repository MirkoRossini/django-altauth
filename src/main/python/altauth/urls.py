from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^set_alternative_password/$',
        'altauth.views.set_alternative_password',
        name='altauth_set_alternative_password'),
    url(
        r'^alternative_password_login/$',
        'altauth.views.alternative_password_login',
        name='altauth_alternative_password_login'),
    url(r'^set_public_key/$', 'altauth.views.set_public_key', name='altauth_set_public_key'),
    url(r'^public_key_login/$', 'altauth.views.public_key_login', name='altauth_public_key_login'),
    url(r'^get_public_key_token/$',
        'altauth.views.get_public_key_token',
        name='altauth_get_public_key_token'),
    # url(r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
