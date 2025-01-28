from django.contrib import admin

from .models import Index, Steps, Contact, Form
from django.utils.html import format_html
# Register your models here.

admin.site.register(Index)



@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')

@admin.register(Steps)
class StepsAdmin(admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height=50px />'.format(obj.img.url))
    
    image_tag.short_description = 'Фото'
    
    list_display = ('title', 'image_tag',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("title", 'description')
# Register your models here.
