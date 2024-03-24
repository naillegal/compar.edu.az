from django.utils.text import slugify
from django.utils.html import format_html


letters_eq = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': '', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'y', 'я': 'ya',
    'ü': 'u', 'ö': 'o', 'ğ': 'g', 'ə': 'e', 'ç': 'c', 'ş': 's', 'ı': 'i'
}
trans = {ord(k): v for k, v in letters_eq.items()}
def get_slug(slug):
    return slugify(slug.lower().translate(trans))

from django.utils.safestring import mark_safe

def get_image_tag(url):
    return mark_safe(format_html('<img src="{}" width="200" style="background-color: white"/>', url))

def get_slug_link(slug, get_absolute_url):
    if slug:
        return mark_safe(format_html('<a href="{0}">{1}{0}</a>', get_absolute_url(), 'https://compar.az'))
    return '-'

