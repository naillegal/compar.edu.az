from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('', views.events_list, name='events'),
    path('<int:pk>/<str:slug>/', views.event_detail, name='event-detail')
]
