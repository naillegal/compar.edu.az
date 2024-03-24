from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('article/<int:pk>/<str:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('tag/<int:pk>/<str:slug>/', views.BlogListView.as_view(), kwargs={'filter_type': 'tag'}, name='blog-tag'),
    path('category/<int:pk>/<str:slug>/', views.BlogListView.as_view(), kwargs={'filter_type': 'category'}, name='blog-category'),
    path('search/', views.BlogListView.as_view(), name='blog-search'),
]
