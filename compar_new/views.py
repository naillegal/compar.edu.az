from django.shortcuts import render, redirect
from django.conf import settings

def handler_error_view(request, *args, **kwargs):
    for lang_code, _ in settings.LANGUAGES:
        if request.path.startswith('/'+lang_code):
            return render(request, 'error.html')
    return redirect('/'+settings.LANGUAGE_CODE+request.path)
        