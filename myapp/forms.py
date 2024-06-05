from django import forms
from .models import Review, Messages

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['email', 'rating', 'comment']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['full_name', 'gender', 'email', 'birth_date', 'message']
