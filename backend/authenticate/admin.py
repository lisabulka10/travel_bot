from django.contrib import admin

from .models import User
from profiles.models import UserProfile


class UserProfileTabular(admin.TabularInline):
    model = UserProfile
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_id', 'username')
    inlines = [UserProfileTabular]
