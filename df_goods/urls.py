from django.conf.urls import url
import views

urlpatterns=[
    url('^$',views.index),
    url('^index2(\d+)/$',views.index2),
    # url('^list/$',views.list),
    # url('^detail/$',views.detail),
]
