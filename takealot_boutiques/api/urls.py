from django.conf.urls import url

from takealot_boutiques.api import views

urlpatterns = [
    url(r'^get_products$', views.get_products, name='get_products'),
]
