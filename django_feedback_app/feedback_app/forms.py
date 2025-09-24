from django import forms

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Your Email", widget=forms.EmailInput(attrs={'class':'form-control'}))
    feedback = forms.CharField(label="Your Feedback", widget=forms.Textarea(attrs={'class':'form-control'}))
