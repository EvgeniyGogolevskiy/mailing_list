from django import forms
from .models import Subscriber


class ChoiceForm(forms.Form):
    choice_subscriber = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                       queryset=Subscriber.objects.all())
    choice_layout = forms.ChoiceField(choices=(("English", "English"), ("German", "German"), ("French", "French")))
    choice_delay_seconds = forms.IntegerField(required=False)
