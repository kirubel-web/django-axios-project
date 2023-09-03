from django.contrib import admin
from .models import Contact

from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    # Customize the display of the Contact model in the admin interface
    list_display = ('name', 'email', 'message')

# Register the Contact model with the ContactAdmin configuration
admin.site.register(Contact, ContactAdmin)
# Register your models here.
