from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'track_expenses.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^managetool/$','admintool.views.admin_view'),
    url(r'^$','admintool.views.admin_view'),
    url(r'^timenow/$','admintool.views.time_display')
)
