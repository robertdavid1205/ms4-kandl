from django.db import models
from django.contrib.auth.models import User

from products.models import Product

# code adapted from pmeeny Paul Meeneghan


class Favorites(models.Model):
    """
    This model is for a users favorites list
    """
    class Meta:
        verbose_name_plural = 'Favorites'

    products = models.ManyToManyField(
        Product,
        blank=True
    )
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        Return object string
        Args:
            self (object): self object.
        Returns:
            str: users favorite string
        """
        return f"{self.username}'s Favorites"
