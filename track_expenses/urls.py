from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'track_expenses.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^managetool/$','admintool.views.admin_view'),
    #url(r'^$','admintool.views.admin_view'),
    url(r'^$',include('admintool.urls')),
    url(r'^timenow/$','admintool.views.time_display'),
    url(r'^expenditure/', include('admintool.urls')),
    url(r'^add_expense/$','admintool.views.add_expense'),
    url(r'^save_expense/$', 'admintool.views.save_expense'),
    url(r'^delete_expense/$', 'admintool.views.delete_expense'),
    url(r'^update_expense/$', 'admintool.views.update_expense'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
)

