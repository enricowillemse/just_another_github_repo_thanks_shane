from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from takealot_boutiques.models import UserProducts, UserOrders


@login_required
def list_products(request):
    current_user = request.user
    product_results = []
    user_products = UserProducts.objects.filter(user_email=current_user).all()
    for user_product in user_products:
        product_results.append(user_product.product)
    data = {}
    data['user_products'] = product_results
    return render(request, 'customer/user_products.html', data)


@login_required
def remove_product(request):
    post_values = request.POST.copy()
    id = post_values['id']
    current_user = request.user
    user_product = UserProducts.objects.filter(product_id=id, user_email=current_user).first()
    if user_product:
        user_product.delete()
    return redirect('/user_products/list_products')


def user_orders(request):
    post_values = request.POST.copy()
    current_user = request.user
    user_orders = UserOrders.objects.filter(user_email=current_user)
    data = {}
    data['user_orders'] = user_orders
    return render(request, 'customer/user_orders.html', data)
