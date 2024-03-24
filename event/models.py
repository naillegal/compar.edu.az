from django.db import models
from shared.urlutils import get_slug
from django.urls import reverse

CATEGORY_CHOICES = [
    ('xəbər', 'Xəbər'),
    ('tədbir', 'Tədbir'),
]

class Events(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Başlıq')
    slug = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=False, blank=False, verbose_name='Mətn')
    image = models.ImageField(upload_to='course/', null=False, blank=False, verbose_name='Şəkil')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES,verbose_name='Kateqoriya')
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Tədbir'
        verbose_name_plural = 'Tədbirlər'

    def __str__(self):
        return self.title + ' tədbir'
    
    def save(self, *args, **kwargs):
        self.slug = get_slug(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"pk": self.pk, 'slug': self.slug})
