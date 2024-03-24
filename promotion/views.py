from django.shortcuts import redirect, render
from django.urls import reverse
from promotion.forms import AppointmentForm
from blog.models import Article
from promotion.models import Slider, StudentReview, Alumni, StudentProject, StudentProjectTag, AboutStatictic, Faq
from os import getenv
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def home(request):
    packages = Article.objects.filter(
        category__title='Tədris Paketləri').order_by('created')
    articles = Article.objects.exclude(category__title='Tədris Paketləri')[:5]
    sliders = Slider.objects.all()
    student_reviews = StudentReview.objects.all()
    student_projects = StudentProject.objects.all()
    student_projects_tags = StudentProjectTag.objects.all()
    alumnies = Alumni.objects.all()
    return render(request, 'home.html', context={
        'packages': packages, 'articles': articles, 'sliders': sliders, 'student_reviews': student_reviews,
        'alumnies': alumnies, 'student_projects': student_projects, 'student_projects_tags': student_projects_tags,
    })


def contact(request, appointment=None):
    return render(request, 'contact.html', context={'appointment': appointment})


def about(request):
    about_statistics = AboutStatictic.objects.all()
    return render(request, 'about.html', context={
        'about_statistics': about_statistics
    })


def faq(request):
    faqs = Faq.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})


def graduates(request):
    alumnies = Alumni.objects.all()
    student_projects = StudentProject.objects.all()
    student_projects_tags = StudentProjectTag.objects.all()
    paginator = Paginator(student_projects, 8)  
    page_number = request.GET.get('page')  

    try:
        student_projects = paginator.page(page_number)
    except PageNotAnInteger:
        student_projects = paginator.page(1)
    except EmptyPage:
        student_projects = paginator.page(paginator.num_pages)

    return render(request, 'graduates.html', context={
        'alumnies': alumnies,
        'student_projects_tags': student_projects_tags,
        'student_projects': student_projects,
        'is_paginated': True, 
        'page_obj': student_projects,  
        'paginator': paginator, 
    })


def method(request):
    return render(request, 'method.html')


def packages(request):
    articles = Article.objects.filter(
        category__title='Tədris Paketləri').order_by('created')
    return render(request, 'customs/promotion/packages.html', context={'articles': articles})


def corporative(request):
    return render(request, 'customs/promotion/corporative.html')


def appointment(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        secret_key = getenv('RECAPTCHA_SECRET_KEY')
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
            'secret': secret_key,
            'response': recaptcha_response
        }).json()
        form = AppointmentForm(request.POST)
        if form.is_valid() and 'score' in response and response.get('score') > 0.7:
            appointment_instance = form.save()
            appointment_instance.save()
            return redirect(reverse('promotion:contact') + '?success=true')
        else:
            return redirect(reverse('promotion:contact') + '?success=false')
    else:
        return redirect('promotion:contact')
    


def privacy(request):
    return render(request, 'customs/promotion/privacy.html')
