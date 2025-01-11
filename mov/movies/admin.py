from django.contrib import admin
from .models import Movies

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'year', 'rating')
    list_filter = ('category', 'year', 'rating')
    search_fields = ('title', 'description', 'category')
    ordering = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'category', 'duration')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('img', 'rating', 'year', 'video'),
        }),
    )
    readonly_fields = ('year',)

admin.site.register(Movies, MoviesAdmin)
