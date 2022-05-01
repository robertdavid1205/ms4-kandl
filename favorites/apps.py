from django.apps import AppConfig


# code adapted from pmeeny Paul Meeneghan

class FavoritesConfig(AppConfig):
    """
    A class for configuring the favorites app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'favorites'
