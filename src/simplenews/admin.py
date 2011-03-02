from django.contrib import admin

from simplenews.models import Article

class ArticleAdmin(admin.ModelAdmin):
    """Admin for the Articles"""
    pass

admin.site.register(Article, ArticleAdmin)
