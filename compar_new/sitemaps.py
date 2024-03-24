from django.contrib import sitemaps
from django.urls import reverse

from blog.models import Article, Tag, Category

class StaticViewSitemap(sitemaps.Sitemap):
    change_freqs = {
        'promotion:home': 'monthly',
        'promotion:about': 'yearly',
        'promotion:faq': 'yearly',
        'promotion:packages': 'monthly',
        'promotion:contact': 'yearly',
        'blog:blog-list': 'weekly'
    }
    priorities = {
        'promotion:home': 1.0,
        'promotion:about': 0.8,
        'promotion:faq': 0.6,
        'promotion:packages': 0.8,
        'promotion:contact': 0.7,
        'blog:blog-list': 0.4
    }

    def items(self):
        return [
            'promotion:home',
            'promotion:about',
            'promotion:faq',
            'promotion:packages',
            'promotion:contact',
            'blog:blog-list',
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return self.priorities.get(item, 0.5)

    def changefreq(self, item):
        return self.change_freqs.get(item, 'never')


class ArticleSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return Article.objects.filter(show=True)

class CategorySitemap(sitemaps.Sitemap):
    priority = 0.3
    changefreq = 'monthly'

    def items(self):
        return Category.objects.all()

class TagSitemap(sitemaps.Sitemap):
    priority = 0.4
    changefreq = 'monthly'

    def items(self):
        return Tag.objects.all()