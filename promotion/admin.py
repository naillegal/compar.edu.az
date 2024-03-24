from django.contrib import admin
from promotion import models

# Register your models here.


@admin.register(models.Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'contact', 'subject', 'message', 'created']
    list_display = ['name', 'contact', 'viewed', 'created']


@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['headline', 'title',]
    search_fields = ['headline', 'title', 'description']
    list_filter = ['updated', 'created']
    readonly_fields = ['created', 'updated']


@admin.register(models.StudentReview)
class StudentReviewAdmin(admin.ModelAdmin):
    list_display = ['full_name',]
    search_fields = ['full_name', 'job_title', 'comment']
    list_filter = ['updated', 'created']
    readonly_fields = ['created', 'updated']


@admin.register(models.Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ['full_name',]
    search_fields = ['full_name', 'job_title']
    list_filter = ['updated', 'created']
    readonly_fields = ['created', 'updated']


@admin.register(models.StudentProject)
class StudentProjectAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title', 'description']
    list_filter = ['updated', 'created']
    readonly_fields = ['created', 'updated']


@admin.register(models.StudentProjectTag)
class StudentProjectTagAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title']
    list_filter = ['updated', 'created']
    readonly_fields = ['created', 'updated']

@admin.register(models.AboutStatictic)
class AboutStaticticAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title',]
    list_filter = ['updated', 'created']
    readonly_fields = ['created', 'updated']

@admin.register(models.Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question',]
    search_fields = ['question',]
    list_filter = ['updated', 'created']
    readonly_fields = ['created', 'updated']


