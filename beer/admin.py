from django.contrib import admin

from .models import Beer, Category, Style


class BeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'style', 'abv')
    search_fields = ('categoty', 'style', 'abv', 'ibu', 'srm')
    exclude = ('slug', 'created_date', 'added_by')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class StyleAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Beer, BeerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Style, StyleAdmin)
