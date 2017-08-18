# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Product ,Family ,Location ,Transaction  
# Register your models here.

admin.site.site_header = "My Product Inventory ";
admin.site.site_title = "My Product Inventory ";


def set_quantity_zero(modelAdmin, request, queryset):
    for product in queryset:
        product.quantity = 0
        product.save()

set_quantity_zero.short_description = 'Set Quantity to Zero'

#class LocationInline(admin.TabularInline):
#    model = Location

#class FamilyInline(admin.TabularInline):
#    model = Family


class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku', 'title', 'unit', 'unitCost', 'quantity']
    list_filter = ('sku', 'unit')
    #fields = [('family','location'),('sku','barcode'), ('title','description'),('unit', 'unitCost'), ('quantity','minQuantity')]
    fieldsets = (
        ('Section 1', {
            'fields': ('family','location')
        }),
        ('Section 2', {
            'fields': ('title','description')
        }),        
        ('Section 3', {
            'fields': ('sku','barcode','unit', 'unitCost','quantity','minQuantity')
        }),
    )
    #inlines = [LocationInline , FamilyInline]
    actions = [set_quantity_zero, ]

admin.site.register(Product , ProductAdmin)
admin.site.register(Family)
admin.site.register(Location)
admin.site.register(Transaction)

