from django.contrib import admin
from apps.users.models import Church


@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'phone', 'email', 'website', 'founded', 'active']
    search_fields = ['name', 'city', 'state', 'phone', 'email', 'website']
    list_filter = ['active']
    date_hierarchy = 'founded'
    filter_horizontal = ['users']
    fieldsets = (
        (None, {
            'fields': ('name', 'address', 'city', 'state', 'zip_code', 'phone', 'email', 'website', 'founded', 'active')
        }),
        ('Usuários', {
            'fields': ('users',)
        })
    )
    readonly_fields = ['founded']
