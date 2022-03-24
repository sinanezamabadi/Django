from django.contrib import admin
from .models import Article
# Register your models here.
class Articleadmin(admin.ModelAdmin):
    list_display = ('title','view', 'published_at')
    date_hierarchy = 'published_at'
    fields=('title', 'body','published_at')


admin.site.register(Article,Articleadmin)

