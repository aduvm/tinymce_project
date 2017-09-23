from django.contrib import admin
from tinymceapp.models import  Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ['title','content']

admin.site.register(Page, PageAdmin)