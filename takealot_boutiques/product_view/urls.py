from django.conf.urls import url

from takealot_boutiques.product_view import views

urlpatterns = [
    url(r'^(?P<product_id>\d+)$', views.view, name='view'),
    url(r'^add_to_products/(?P<product_id>\d+)$', views.add_to_products, name='add_to_products'),
    url(r'^remove_from_products/(?P<product_id>\d+)$', views.remove_from_products, name='remove_from_products')
]
