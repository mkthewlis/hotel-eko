from django.contrib import admin
from .models import Stay, Relax, Eat


class StayAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'no_of_guests',
        'shower_bath',
        'view',
        'has_breakfast',
        'price',
        'image',
    )
    ordering = ('sku',)


class RelaxAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'length',
        'scents',
        'aims',
        'price',
        'image',
    )
    ordering = ('sku',)


class EatAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'protein',
        'no_of_courses',
        'has_gluten',
        'price',
        'image',
    )
    ordering = ('sku',)


admin.site.register(Stay, StayAdmin)
admin.site.register(Relax, RelaxAdmin)
admin.site.register(Eat, EatAdmin)
