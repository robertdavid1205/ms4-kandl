from django.contrib import admin

from .models import Favorites
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# code adapted from pmeeny Paul Meeneghan


class FavoritesAdmin(admin.ModelAdmin):
    """
    Admin class for the Favorites model.
    """
    list_display = (
        'username',
    )
    search_fields = (
        'username',
    )
    list_filter = (
        'username',
    )
    list_per_page = 20


admin.site.register(Favorites, FavoritesAdmin)
