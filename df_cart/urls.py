from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.cart),
    url(r'^add(\d+)_(\d+)/$',views.add),
]