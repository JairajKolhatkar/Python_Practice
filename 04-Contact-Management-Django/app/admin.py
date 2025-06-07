from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact
# Temporarily commented out to fix dependency issues
# from import_export.admin import ImportExportModelAdmin

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'email', 'phone', 'info', 'date_added')
    list_display_links = ('id', 'name')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name', 'gender', 'email', 'phone', 'info')
    list_filter = ('gender', 'date_added')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'email', 'phone', 'gender')
        }),
        ('Additional Information', {
            'fields': ('info', 'image')
        }),
        ('Relationship', {
            'fields': ('manager',)
        }),
    )

admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)

