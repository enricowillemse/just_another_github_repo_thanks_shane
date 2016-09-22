from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from takealot_boutiques.user_products import views

urlpatterns = [
    url(r'^list_products$', views.list_products, name='list_products'),
    url(r'^remove_product$', csrf_exempt(views.remove_product), name='remove_product'),
    url(r'^user_orders$', views.user_orders, name='user_orders')
]
