from django import forms
from ..models import Review, Inquiry

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['client_name', 'client_email', 'rating', 'comment']
        widgets = {
            'client_name': forms.TextInput(attrs={'placeholder': 'Your Name *'}),
            'client_email': forms.EmailInput(attrs={'placeholder': 'Your Email (optional)'}),
            'rating': forms.Select(choices=[
                (5, '★★★★★ Excellent'),
                (4, '★★★★☆ Good'),
                (3, '★★★☆☆ Average'),
                (2, '★★☆☆☆ Poor'),
                (1, '★☆☆☆☆ Very Poor'),
            ]),
            'comment': forms.Textarea(attrs={'placeholder': 'Share your experience...', 'rows': 4}),
        }

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'service_category', 'location', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. John Kamau'}),
            'email': forms.EmailInput(attrs={'placeholder': 'john@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+254 700 000 000'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. Westlands, Nairobi'}),
            'message': forms.Textarea(attrs={'placeholder': 'Describe your project — what you need, timeline, budget range...', 'rows': 4}),
        }
