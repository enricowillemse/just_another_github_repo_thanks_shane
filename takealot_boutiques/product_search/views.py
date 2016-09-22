from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from takealot_boutiques.models import Products
from django.db.models import Q

SEARCH_API = "https://api.takealot.com/rest/v-1-4-4"


@login_required
def result(request):
    data = {}
    post_values = request.POST.copy()
    query = post_values['query']
    products = Products.objects.filter(Q(title__search=query) | Q(description__search=query))[:30]
    data['products'] = products
    return render(request, 'customer/product_search.html', data)
