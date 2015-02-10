from django.conf.urls import patterns, include, url
from admintool import views, json_views

urlpatterns = patterns('admintool.views',
    url(r'^$', views.index, name='index'),
    url(r'^add/$',views.add_expense, name = 'add_expense'),
    url(r'^save/$', views.save_expense, name = 'save_expense'),
    url(r'^delete/$', views.delete_expense, name = 'delete_expense'),
    url(r'^update/$', views.update_expense, name = 'update_expense'),
    url(r'^upload/$', views.upload_target, name = 'upload_expense_csv'),
    url(r'^expense_categories/$', json_views.expenseCategory_list, name = 'expenseCategory_list' ),
    url(r'^expense_categories/(?P<pk>[0-9]+)$', json_views.expenseCategory_detail, name ='expenseCategory_detail' ), 
   
)
