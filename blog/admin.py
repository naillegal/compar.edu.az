from django.contrib import admin
from blog import models
from django.db import models as model_class
from django.forms import Textarea

# Register your models here.
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ('title', 'slug_link', 'updated', 'created')
    readonly_fields = ('updated', 'created', 'slug_link')
    list_display = ('title', 'slug_link', 'updated', 'created')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'slug_link', 'updated', 'created')
    readonly_fields = ('updated', 'created', 'slug_link')
    list_display = ('title', 'slug_link', 'updated', 'created')


class ArticleImageInline(admin.TabularInline):
    fields = ('image_file_tag', 'image_file', 'updated', 'created')
    model = models.ArticleImage
    readonly_fields = ('updated', 'created', 'image_file_tag')
    extra = 1

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'content', 'main_image_tag', 'main_image',
    'vector_image_tag', 'vector_image', 'tags', 'category', 'viewed', 'show', 'slug_link', 'updated', 'created')
    readonly_fields = ('main_image_tag', 'vector_image_tag', 'viewed', 'updated', 'created', 'slug_link')
    formfield_overrides = {
        model_class.TextField: {'widget': Textarea(attrs={'rows':2, 'style': 'width: 60%'})},
    }
    list_display = ('title', 'show', 'viewed', 'category_title', 'updated', 'created')
    inlines = [ArticleImageInline]