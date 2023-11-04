from django.contrib import admin
from .models import MenuItem
from mptt.admin import MPTTModelAdmin

class MenuInLine(admin.TabularInline):
    model = MenuItem
    prepopulated_fields = {"url": ("title",)}


@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):
    list_display = ['title', 'url', 'parent', 'active']
    inlines = (MenuInLine,)

