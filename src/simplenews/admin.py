from django.contrib import admin

from simplenews.models import Article, ArticleImage

class ArticleImageInline(admin.StackedInline):
    model = ArticleImage

class ArticleAdmin(admin.ModelAdmin):
    """Admin for the Articles"""
    list_display = ['title', 'status', 'is_featured', 'created']
    date_hierarcy = 'created'
    list_filter = ['created', 'status', 'is_featured']
    inlines = [ArticleImageInline, ]

admin.site.register(Article, ArticleAdmin)
