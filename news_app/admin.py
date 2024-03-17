from django.contrib import admin
from .models import News,Category,Contact,Fotografiya

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','category','status','created_time']
    list_filter = ['created_time','publish_time','status']
    prepopulated_fields = {"slug":('title',)}
    search_fields = ['title']
    ordering = ['status','created_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']

@admin.register(Fotografiya)
class FotografiyaAdmin(admin.ModelAdmin):
    list_display = ['name','author','image']