from django.http import Http404
from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from products.models import Product
from .models import Favorites

# Create your views here.
# code adapted from pmeeny Paul Meeneghan

@login_required
def view_product_favorites(request):
    """
    A view that displays users favorites
    Args:
        request (object): HTTP request object.
    Returns:
        Renders the request, template and context
    """
    favorites_items_count = 0
    try:
        all_favorites = Favorites.objects.filter(username=request.user.id)[0]
    except IndexError:
        favorites_items = None
    else:
        favorites_items = all_favorites.products.all()
        favorites_items_count = all_favorites.products.all().count()
        favorites_items = setup_pagination(favorites_items, request, 4)

    if not favorites_items:
        messages.info(request, 'Your favorites list is empty!')

    template = 'favorites/favorites.html'
    context = {
        'favorites_items': favorites_items,
        'favorites_items_count': favorites_items_count
    }
    return render(request, template, context)


@login_required
def add_product_to_favorites(request, item_id):
    """
    Add a product item to favorites
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        favorites = get_object_or_404(Favorites, username=request.user.id)
    except Http404:
        favorites = Favorites.objects.create(username=request.user)
    if product in favorites.products.all():
        messages.info(request, 'The product is '
                               'already in your favorites!')
    else:
        favorites.products.add(product)
        messages.info(request, 'Added the product to your favorites')
    return redirect(reverse('product_detail', args=[item_id]))


@login_required
def remove_product_from_favorites(request, item_id, redirect_from):
    """
    Remove a product item from favorites
    """
    product = get_object_or_404(Product, pk=item_id)
    favorites = get_object_or_404(Favorites, username=request.user.id)
    if product in favorites.products.all():
        favorites.products.remove(product)
        messages.info(request, 'Removed the product '
                               'from your favorites list')
    else:
        messages.error(request, 'That product is '
                                'not in your favorites list!')
    if redirect_from == 'favorites':
        redirect_url = reverse('view_product_favorites')
    else:
        redirect_url = reverse('product_detail', args=[item_id])
    return redirect(redirect_url)
