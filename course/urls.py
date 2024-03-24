from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<int:pk>/<str:slug>/', views.course_detail, name='course-detail'),
]
