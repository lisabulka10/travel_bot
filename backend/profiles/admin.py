from django.contrib import admin

from .models import UserProfile, Activity, ProfileActivity


class ProfileActivityInline(admin.TabularInline):
    model = ProfileActivity
    extra = 1
    fields = ('activity', 'priority')
    ordering = ('priority',)


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'budget_min', 'budget_max')
    inlines = [ProfileActivityInline]


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


