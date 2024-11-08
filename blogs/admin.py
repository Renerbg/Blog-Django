from django.contrib import admin
from blogs.models import Post, Category, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('title',), }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('title',), }

admin.site.register(Comment)
