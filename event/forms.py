from django import forms
from .models import EventApply

class EventApplyForm(forms.ModelForm):
    
    class Meta:
        model = EventApply
        exclude = ('declined', 'event')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'comment-form-input', 'placeholder': 'Ad Soyad'}),
            'email': forms.TextInput(attrs={'class': 'comment-form-input', 'placeholder': 'Email Ünvanı'}),
            'phone': forms.TextInput(attrs={'class': 'comment-form-input', 'placeholder': 'Telefon Nömrəsi'}),
        }
    
    def save(self, event):
        event_apply = EventApply(event=event, **self.cleaned_data)
        event_apply.save()
        return event_apply