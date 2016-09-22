from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from takealot_boutiques.models import Products, UserProducts


@login_required
def view(request, product_id):
    product = Products.objects.get(id=product_id)
    data = {}
    data['product'] = product
    return render(request, 'customer/product_view.html', data)


def add_to_products(request, product_id):
    post_values = request.POST.copy()
    product = Products.objects.get(id=product_id)
    user_product = UserProducts()
    user_product.product = product
    current_user = request.user
    user_product.user_email = current_user
    user_product.save()
    return redirect('/product_view/' + product_id)


def remove_from_products(request, product_id):
    post_values = request.POST.copy()
    current_user = request.user
    user_product = UserProducts.objects.get(product_id=product_id, user_email=current_user)
    if user_product:
        user_product.delete()
        user_product.save()
    return redirect('/product_view/' + product_id)
