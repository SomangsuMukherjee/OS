from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'faculty', 'review', 'image']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
