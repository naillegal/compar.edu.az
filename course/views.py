from django.shortcuts import render, get_object_or_404
from .models import Course, CourseOpportunity, CourseTeacher, CourseSyllabus


def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', context={'courses': courses})


def course_detail(request, pk, slug):
    course = get_object_or_404(Course, pk=pk, slug=slug)
    courses = Course.objects.all()
    course_syllabi = CourseSyllabus.objects.filter(course=course)
    course_teachers = CourseTeacher.objects.filter(courses=course)
    course_opportunities = CourseOpportunity.objects.filter(course=course)
    return render(request, 'course-detail.html', context={
        'course': course,
        'course_syllabi': course_syllabi,
        'course_teachers': course_teachers,
        'course_opportunities': course_opportunities,
        'courses': courses,
    })
