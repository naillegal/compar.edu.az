from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from utils.model.field_utils import get_image_tag, get_slug, get_slug_link
from imagekit.models import ProcessedImageField
from django.utils import timezone
from minify_html import minify
from django.contrib.admin import display


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Ad')
    updated = models.DateField(auto_now = True, verbose_name='Dəyişdirildi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradıldı')

    class Meta:
        ordering = ['-updated']
        verbose_name = 'Teq'
        verbose_name_plural = 'Teqlər'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog-tag", kwargs={'pk': self.pk, 'slug': self.slug})

    @property
    def slug(self):
        return get_slug(self.title) if self.title and self.pk else None

    @display(description='Link')
    def slug_link(self):
        return get_slug_link(self.slug, self.get_absolute_url)

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Ad')
    updated = models.DateField(auto_now = True, verbose_name='Dəyişdirildi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradıldı')
    class Meta:
        ordering = ['-updated']
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog-category", kwargs={'pk': self.pk, 'slug': self.slug})


    @property
    def slug(self):
        return get_slug(self.title) if self.title and self.pk else None

    @display(description='Link')
    def slug_link(self):
        return get_slug_link(self.slug, self.get_absolute_url)



class Article(models.Model):
    title = models.TextField(verbose_name='Başlıq')
    slug = models.SlugField(verbose_name='Slug', null=True, blank=True, max_length=100)
    description = models.TextField(verbose_name='Açıqlama')
    content = RichTextField(verbose_name='Kontent')
    main_image =ProcessedImageField(upload_to='blog/article/', options={'quality': 70}, verbose_name='Əsas Şəkil')
    vector_image = ProcessedImageField(upload_to='blog/article-vector/', options={'quality': 70}, verbose_name='Vektor Şəkli', null=True, blank=True, default=None)
    tags = models.ManyToManyField(Tag, verbose_name='Teqlər')
    viewed = models.IntegerField(default=0, verbose_name='İzlənilmə Sayı')
    show = models.BooleanField(default=True, verbose_name='Göstərilsin')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)
    updated = models.DateField(default=None, null=True, blank=True, verbose_name='Dəyişdirildi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradıldı')

    class Meta:
        ordering = ['-updated']
        verbose_name = 'Məqalə'
        verbose_name_plural = 'Məqalələr'

    def __str__(self):
        return self.title

    def save(self, const_updated_date=False):
        if not const_updated_date:
            self.updated = timezone.localdate()
            self.content = minify(self.content)
            self.slug = get_slug(self.title) if self.title and self.pk else None
        return super().save()
    
    @display(description='Mövcud Əsas Şəkil')
    def main_image_tag(self):
        return get_image_tag(self.main_image.url)

    @display(description='Mövcud Vektor Şəkli')
    def vector_image_tag(self):
        return get_image_tag(self.vector_image.url)

    @display(description='Kateqoriya')
    def category_title(self):
        return self.category.title

    @display(description='Link')
    def slug_link(self):
        return get_slug_link(self.slug, self.get_absolute_url)
    
    def get_absolute_url(self):
        return reverse("blog:blog-detail", kwargs={"pk": self.pk, 'slug': self.slug})
    

    def related_articles(self, count=5):
        return Article.objects.filter(tags__in=self.tags.all()
        ).annotate(common_tags_count=models.Count('pk')).order_by('-common_tags_count'
        ).exclude(pk=self.pk)[:count]

    def get_image(self):
        if self.vector_image:
            return self.vector_image.url
        else:
            return self.main_image.url

    def get_seo_title(self):
        length = len(self.title)
        if length > 59:
            return self.title[:56] + '...'
        elif length < 9:
            return self.title + ' - Compar Academy İxtisaslaşmış Tədris Mərkəziniz'
        elif length < 19:
            return self.title + ' - Compar Academy İxtisaslaşmış Tədris'
        elif length < 29:
            return self.title + ' - Compar Academy Tədirs Mərkəzi'
        elif length < 39:
            return self.title + ' - Compar Academy'
        elif length < 49:
            return self.title + ' - Compar'
        else:
            return self.title


class ArticleImage(models.Model):
    image_file = ProcessedImageField(upload_to='blog/article-image/', options={'quality': 50})
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    updated = models.DateField(auto_now = True, verbose_name='Dəyişdirildi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradıldı')

    def image_file_tag(self):
        return get_image_tag(self.image_file.url)
    image_file_tag.short_description = 'Mövcud Əsas Şəkil'

    def __str__(self):
        return f'"{self.article.title}" məqalə şəkli'
