from django.urls import path
from promotion import views

app_name = 'promotion'
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('graduates/', views.graduates, name='graduates'),
    path('method/', views.method, name='method'),
    path('packages/', views.packages, name='packages'),
    path('corporative/', views.corporative, name='corporative'),
    path('appointment/', views.appointment, name='appointment'),
    path('privacy/', views.privacy, name='privacy'),
]
