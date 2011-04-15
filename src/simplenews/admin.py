from django.contrib import admin

from simplenews.models import Article, ArticleImage


class ArticleImageInline(admin.StackedInline):
    model = ArticleImage

class ArticleAdmin(admin.ModelAdmin):
    """Admin for the Articles"""
    inlines = [ArticleImageInline, ]

admin.site.register(Article, ArticleAdmin)
