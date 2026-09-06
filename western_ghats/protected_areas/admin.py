from django.contrib import admin
from django.utils.html import format_html
from .models import ProtectedArea


@admin.register(ProtectedArea)
class ProtectedAreaAdmin(admin.ModelAdmin):
    # Columns shown in the list table
    list_display = (
        'name',
        'category',
        'state',
        'district',
        'established_year',
        'area_sq_km',
        'website_link'
    )
    
    # Filters available on the right sidebar
    list_filter = ('category', 'state')
    
    # Search bar fields
    search_fields = ('name', 'district', 'state')
    
    # Group fields into neat sections inside the editor screen
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'official_website')
        }),
        ('Location Details', {
            'fields': ('state', 'district', ('latitude', 'longitude'))
        }),
        ('Park Statistics', {
            'fields': (('established_year', 'area_sq_km'),)
        }),
    )

    # Clickable link column method
    @admin.display(description='Official Website')
    def website_link(self, obj):
        if obj.official_website:
            return format_html('<a href="{}" target="_blank">Visit Site 🔗</a>', obj.official_website)
        return "N/A"