from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Article, Tag, Category
from utils.model.view.pagination import get_page_list
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Count
from django.db.models import F

# Create your views here.
def blog_list(request):
    return render(request, 'blog.html')

def blog_detail(request):
    return render(request, 'blog-detail.html')


class BlogListView(ListView):
    paginate_by = 6
    template_name = 'blog.html'
    context_object_name = 'articles'
    queryset = Article.objects.all().filter(show=True).order_by('-created')

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        keyword = self.request.GET.get('keyword')
        if pk and self.kwargs.get('filter_type') == 'tag':
            return super().get_queryset().filter(tags=pk)
        elif pk and self.kwargs.get('filter_type') == 'category':
            return super().get_queryset().filter(category=pk)
        elif keyword:
            vector = SearchVector('title', weight='A') + SearchVector('description', weight='B') + SearchVector('content', weight='C')
            query = SearchQuery(keyword)
            rank = SearchRank(vector, query)
            return super().get_queryset().annotate(rank=rank).filter(rank__gt=0).order_by('-rank')
        else:
            return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = context['page_obj']
        context['page_list'] = get_page_list(page_obj.number, page_obj.paginator.num_pages, self.paginate_by)
        context['tags'] = Tag.objects.all().annotate(article_count=Count('article'))
        context['categories'] = Category.objects.all()
        context['all_article_count'] = Article.objects.count()
        context['popular_articles'] = Article.objects.all().order_by('-viewed')[:5]
        context['keyword'] = self.request.GET.get('keyword', '')
        if self.kwargs.get('filter_type'):
            blog_title = self.kwargs.get('slug').capitalize()
        else:
            blog_title = 'Bloq'

        context['blog_title'] = blog_title
        
        return context


class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    context_object_name = 'article'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()
        object.viewed = F('viewed') + 1
        object.save(const_updated_date=True)
        current_pk = object.pk
        context['prev_article'] = self.model.objects.filter(pk__lt=current_pk).order_by('-pk').first()
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all().annotate(article_count=Count('article'))
        context['all_article_count'] = Article.objects.count()
        context['popular_articles'] = Article.objects.all().order_by('-viewed')[:5]
        context['next_article'] = self.model.objects.filter(pk__gt=current_pk).order_by('pk').first()
        return context
