from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Admin class for the Contact model.
    """
    list_display = (
        'name', "email", "subject",
    )


admin.site.register(Contact, ContactAdmin)
