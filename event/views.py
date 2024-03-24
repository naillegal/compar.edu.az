from django.shortcuts import render, get_object_or_404
from .models import Events

def events_list(request):
    events = Events.objects.all()
    return render(request, 'events.html', {'events': events})

def event_detail(request, pk, slug):
    event = get_object_or_404(Events, pk=pk, slug=slug)
    return render(request, 'event-detail.html', {'event': event})


