from django.urls import path
from . import views


# code adapted from pmeeny Paul Meeneghan


urlpatterns = [
    path('view_product_favorites/', views.view_product_favorites,
         name='view_product_favorites'),
    path('add_product_to_favorites/<item_id>/',
         views.add_product_to_favorites, name='add_product_to_favorites'),
    path('remove_product_from_favorites/<item_id>/<redirect_from>/',
         views.remove_product_from_favorites,
         name='remove_product_from_favorites'),
]
