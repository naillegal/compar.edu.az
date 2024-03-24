from django.contrib import admin
from . import models

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ['title', 'updated', 'created']
    readonly_fields = ['updated', 'created']
    list_display = ['title', 'updated', 'created']

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    search_fields = ['title']
    list_filter = ['title']

@admin.register(models.Lesson) 
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name'] 
    search_fields = ['name']

@admin.register(models.CourseOpportunity)
class CourseOpportunityAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    search_fields = ['title']

@admin.register(models.CourseSyllabus)
class CourseSyllabusAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'created', 'updated']
    search_fields = ['title']
    list_filter = ['course']

@admin.register(models.CourseTeacher)
class CourseTeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'job_title', 'created', 'updated']
    search_fields = ['full_name']

