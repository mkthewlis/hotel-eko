from django.contrib import admin
from .models import Category, Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'description',
        'image',
        'is_stay',
        'no_of_guests',
        'has_breakfast',
        'is_relax',
        'length',
        'scents',
        'is_eat',
        'protein',
        'no_of_courses',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
