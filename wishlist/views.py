from products.models import Product
from django.contrib import messages
from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)


# Create your views here.


def view_wishlist(request):
    """ A view that renders the wishlist contents page """

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    """ Add a quantity of the specified product to the wishlist """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    wishlist = request.session.get('wishlist', {})

    if size:
        if item_id in list(wishlist.keys()):
            if size in wishlist[item_id]['items_by_size'].keys():
                wishlist[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'Updated size {size.upper()} {product.name} \
                       quantity to {wishlist[item_id]["items_by_size"][size]}')
            else:
                wishlist[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Added size {size.upper()} {product.name} \
                      to your wishlist')
        else:
            wishlist[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'Added size {size.upper()} {product.name} \
                   to your wishlist')
    else:
        if item_id in list(wishlist.keys()):
            wishlist[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} \
                quantity to {wishlist[item_id]}')
        else:
            wishlist[item_id] = quantity
            messages.success(request, f'Added {product.name} \
               to your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)


def adjust_wishlist(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    wishlist = request.session.get('wishlist', {})

    if size:
        if quantity > 0:
            wishlist[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, f'Updated size {size.upper()} {product.name} \
                   quantity to {wishlist[item_id]["items_by_size"][size]}')
        else:
            del wishlist[item_id]['items_by_size'][size]
            if not wishlist[item_id]['items_by_size']:
                wishlist.pop(item_id)
            messages.success(
                request, f'Removed size {size.upper()} {product.name} \
                from your wishlist')
    else:
        if quantity > 0:
            wishlist[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} \
                   quantity to {wishlist[item_id]}')
        else:
            wishlist.pop(item_id)
            messages.success(
                request, f'Removed {product.name} \
                from your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(reverse('view_wishlist'))


def remove_from_wishlist(request, item_id):
    """Remove the item from the shopping wishlist"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        wishlist = request.session.get('wishlist', {})

        if size:
            del wishlist[item_id]['items_by_size'][size]
            if not wishlist[item_id]['items_by_size']:
                wishlist.pop(item_id)
            messages.success(
                request, f'Removed size {size.upper()} {product.name} \
                   from your wishlist')
        else:
            wishlist.pop(item_id)
            messages.success(
                request, f'Removed {product.name} \
                from your wishlist')

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
