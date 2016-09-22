from django.conf.urls import url

from takealot_boutiques.product_search import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', csrf_exempt(views.result), name='result')
]
