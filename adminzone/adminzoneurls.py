from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^adminhome',views.adminhome,name='adminhome'),
    url(r'^product',views.product,name='product'),
    url(r'^customer',views.customer,name='customer'),
    url(r'^enquiry',views.enquiry,name='enquiry'),
    url(r'^afeedback',views.afeedback,name='afeedback'),
    url(r'^acomplain',views.acomplain,name='acomplain'),
    url(r'^achangepassword',views.achangepassword,name='achangepassword'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^adminchangepwd',views.adminchangepwd,name='adminchangepwd'),
    url(r'^deletecomplain/(?P<id>\d+)$',views.deletecomplain,name='deletecomplain'),
    url(r'^deletefeedback/(?P<id>\d+)$',views.deletefeedback,name='deletefeedback'),
    url(r'^deleteenquiry/(?P<id>\d+)$',views.deleteenquiry,name='deleteenquiry'),
    url(r'^addnotification',views.addnoticication,name='addnotification'),
    url(r'^deletenotification/(?P<id>\d+)$',views.deletenotification,name='deletenotification'),
    url(r'^addproduct',views.addproduct,name='addproduct'),
    url(r'^deletecustomer/(?P<eid>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.deletecustomer,name='deletecustomer'),
]