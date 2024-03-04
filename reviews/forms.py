from django import forms

# Import the model
from .models import Review

# Create our Django form

# class ReviewForm(forms.Form):
#     user_name = forms.CharField()

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=50)


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=20,
#                                 error_messages={
#                                     "required": "The name cannot be empty",
#                                     "max_length": "Please enter a shorter name"
#                                 })


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=20,
#                                 error_messages={
#                                     "required": "The name cannot be empty",
#                                     "max_length": "Please enter a shorter name"
#                                 })
#     review_text = forms.CharField(
#         label="Your feedback", widget=forms.Textarea, max_length=100)
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)


# Now using ModelForm

# class ReviewForm(forms.ModelForm):
#     # Add Meta class to customize behaviour
#     class Meta:
#         model = Review
#         # fields = ['user_name', 'review_text', 'rating']
#         fields = '__all__'
#         # exclude = ['rating']

# Customizing the form with custom labels and error messages
class ReviewForm(forms.ModelForm):
    # Add Meta class to customize behaviour
    class Meta:
        model = Review
        # fields = ['user_name', 'review_text', 'rating']
        fields = '__all__'
        # exclude = ['rating']

        # Custom labels
        labels = {
            "user_name": "Your name",
            "review_text": "Your review",
            "rating": "Your rating"
        }

        # Custom error messages for fields
        error_messages = {
            "user_name": {
                "required": "Your name cannot be empty",
                "max_length": "Please enter a shorter name"
            }
        }