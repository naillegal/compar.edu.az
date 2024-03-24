from django import template
from course.models import CourseTeacher

register = template.Library()

@register.simple_tag
def get_teachers():
    return CourseTeacher.objects.all()