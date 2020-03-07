from django.contrib import admin
from .models import Journal, Category, Tag

admin.site.register(Journal)
admin.site.register(Category)
admin.site.register(Tag)
