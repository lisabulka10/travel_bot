from django.contrib import admin

from .models import VisaType, Country, CountryVisa


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'climate', 'created_at', 'updated_at')


@admin.register(VisaType)
class VisaTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
