# # reviews/forms.py
from django import forms
from .models import Review

# class ReviewForm(forms.ModelForm):
#     rating = forms.IntegerField(min_value=1, max_value=10, label="Evaluează calitatea generală a serviciului medical")

#     class Meta:
#         model = Review
#         fields = ['rating', 'text', 'anonymous']
#         widgets = {
#             'text': forms.Textarea(attrs={'rows': 4}),
#         }
class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
        min_value=1,
        max_value=10,
        label=""  # lăsăm gol, ca să nu mai apară "Evaluează calitatea generală..."
    )

    class Meta:
        model = Review
        fields = ['rating', 'text', 'anonymous']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }
