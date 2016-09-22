"""takealot_boutiques URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login

import takealot_boutiques.api.urls
import takealot_boutiques.product_search.urls
import takealot_boutiques.product_view.urls
import takealot_boutiques.user_products.urls
import views

urlpatterns = [
    url(r'^$', views.index, {}, 'index'),
    url(r'^user_products/', include(takealot_boutiques.user_products.urls)),
    url(r'^product_search/', include(takealot_boutiques.product_search.urls)),
    url(r'^product_view/', include(takealot_boutiques.product_view.urls)),
    url(r'^api/', include(takealot_boutiques.api.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.register, {}, 'register'),
    url(r'^login$', login, {
        'template_name': 'login.html'
    }, name='login'),
]
