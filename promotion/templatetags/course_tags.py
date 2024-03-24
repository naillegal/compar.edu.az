from django import template
from course.models import Course

register = template.Library()

@register.simple_tag
def get_courses():
    return Course.objects.all()