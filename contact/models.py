from django.db import models

# Create your models here.
class Contact(models.Model):
    """
    This model is for a user to contact us
    """

    name = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )

    email = models.EmailField(
        max_length=256,
        blank=False,
        null=False
    )

    subject = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )

    message = models.TextField(
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name
