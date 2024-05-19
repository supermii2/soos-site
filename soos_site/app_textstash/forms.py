from django import forms

class StashForm(forms.Form):
    title = forms.CharField(max_length=100, label='Title')
    content = forms.CharField(widget=forms.Textarea, label='Message', required=False)