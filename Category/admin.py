from django.contrib import admin

from Category.models import Category, CompletedCategory

admin.site.register(Category)
admin.site.register(CompletedCategory)
