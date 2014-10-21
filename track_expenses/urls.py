from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'track_expenses.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^managetool/$','admintool.views.admin_view'),
    #url(r'^$','admintool.views.admin_view'),
    url(r'^$',include('admintool.urls')),
    #url(r'^timenow/$','admintool.views.time_display'),
    url(r'^expenses/', include('admintool.urls')),
#    url(r'^add_expense/$',include('admintool.urls')),
#    url(r'^save_expense/$', include('admintool.urls')),
#    url(r'^delete_expense/$', include('admintool.urls')),
#    url(r'^update_expense/$', include('admintool.urls')),
    url(r'^upload_target/$', 'admintool.views.upload_target'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
)

