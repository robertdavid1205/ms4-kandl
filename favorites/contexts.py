from django.http import Http404
from django.shortcuts import get_object_or_404

# Internal:
from .models import Favorites
# code adapted from pmeeny Paul Meeneghan


def wishlist_contents(request):
    """
    A context for Favorites to display count in users navbar
    """
    try:
        favorites = get_object_or_404(Favorites, username=request.user.id)
        favorites_items = favorites.products.all()
        favorites_count = len(favorites_items)
    except Http404:
        favorites_count = None

    context = {
        'favorites_count': favorites_count,
    }

    return context
