import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from takealot_boutiques.models import UserProducts, UserOrders


@login_required
def get_products(request):
    current_user = request.user
    user_products = UserProducts.objects.filter(user_email=current_user)
    products = UserProducts.objects.all()
    product_results = []
    for user_product in products:
        product = user_product.product
        product_results.append({"id": product.id, "product_id": product.product_id, "title": product.title,
                                "description": product.description, "cost_price": product.cost_price,
                                "active": product.active, "stock": product.stock, "barcode": product.barcode})
    return JsonResponse(product_results, safe=False)


def new_purchase_order(request):
    data = {}
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    user_order = UserOrders()
    current_user = request.user
    user_order.user_email = current_user
    user_order.customer_products = body['customer_products']
    user_order.customer_address = body['customer_address']
    user_order.customer_name = body['customer_name']
    user_order.customer_phone = body['customer_phone']
    user_order.customer_email = body['customer_email']
    user_order.order_status = "order_recieved"
    return JsonResponse(data, safe=False)


def cancel_purchase_order(request):
    data = {}
    post_values = request.POST.copy()
    current_user = request.user
    purchase_order_id = post_values['purchase_order_id']
    user_order = UserOrders.objects.filter(id=purchase_order_id, user_email=current_user)
    if user_order:
        user_order.order_status = "cancelled"
        user_order.save()
    return JsonResponse(data, safe=False)
