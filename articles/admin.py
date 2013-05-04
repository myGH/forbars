from django.contrib import admin
from articles.models import Comment, Article

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    fields = ['date_change', 'title', 'article_text']
    inlines = [CommentInline]
    list_display = ('title', 'article_text', 'date_change')
    search_fields = ['title']
    date_hierarchy = 'date_change'

admin.site.register(Article, ArticleAdmin)


