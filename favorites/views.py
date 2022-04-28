from django.http import Http404
from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from products.models import Product
from util.util import setup_pagination
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