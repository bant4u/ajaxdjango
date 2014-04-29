from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ajaxtesting.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'ajaxtesting.views.hello'),
    url(r'^home/', 'ajaxtesting.views.home'),
    url(r'^edit/', 'ajaxtesting.views.edit'),
)
