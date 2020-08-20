from django.contrib import admin
from . models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','writer','publish','status')
    list_filter=('status','writer','publish')
    search_fields=('title','body')
    raw_id_fields=('writer',)
    prepopulated_fields={'slug':('title',)}
    list_editable=('status',)





admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)

# Register your models here.
