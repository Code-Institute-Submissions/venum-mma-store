from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def wishlist_contents(request):

    wishlist_items = []
    product_count = 0

    context = {
        'wishlist_items': wishlist_items,
        'product_count': product_count,
    }

    return context
