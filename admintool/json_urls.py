from django.conf.urls import patterns, include, url
from admintool import views, json_views

urlpatterns = patterns('admintool.json_views',
    url(r'^expenses/$', json_views.ExpenseCollection.as_view()),
    url(r'^expenses/(?P<pk>[0-9]+)$', json_views.ExpenseDetail.as_view()), 
    url(r'^expense_categories/$', json_views.expenseCategory_list, name = 'expenseCategory_list' ),
    url(r'^expense_categories/(?P<pk>[0-9]+)$', json_views.expenseCategory_detail, name ='expenseCategory_detail' ),   
    url(r'^expense/(?P<vendor_name>.+)/$',  json_views.expense_filterByVendor,  name='expense_filterByVendor' ), 
    url(r'^expenseByDate/([0-9]{4})/([0-9]{2})/$', json_views.expense_filterByDate, name='expense_filterByDate'),
    url(r'^expenseByDateVendor/([0-9]{4})/([0-9]{2})/([A-Za-z]+)/$', json_views.expense_filterByDateVendor, name='expense_filterByDateVendor'),

)
