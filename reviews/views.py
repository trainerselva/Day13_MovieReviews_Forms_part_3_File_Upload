from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review

from django.views import View

# Create your views here.

# def review(request):
#     return render(request, "reviews/review.html")

# Extract form data and show thank you page
# def review(request):
#     if request.method == 'POST':
#         entered_username = request.POST['username']
#         print(entered_username)
#         return HttpResponseRedirect("/thank-you")
    
#     return render(request, "reviews/review.html")

# Manual form validation
# def review(request):
#     if request.method == 'POST':
#         entered_username = request.POST['username']

#         if entered_username == "":
#             return render(request, "reviews/review.html", {
#                 "has_error": True
#             })
        
#         print(entered_username)
#         return HttpResponseRedirect("/thank-you")
    
#     return render(request, "reviews/review.html", {
#         "has_error": False
#     })


# Use the ReviewForm (django form)
# def review(request):
#     myform = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": myform
#     })

# Add form validation logic
# def review(request):
#     myform = ReviewForm()

#     if request.method == 'POST':
#         myform = ReviewForm(request.POST)

#         if myform.is_valid():
#             print(myform.cleaned_data)
#             return HttpResponseRedirect("/thank-you")
        
#     return render(request, "reviews/review.html", {
#         "form": myform
#     })

#     return render(request, "reviews/review.html", {
#         "form": myform
#     })

# def review(request):
#     if request.method == 'POST':
#         myform = ReviewForm(request.POST)

#         if myform.is_valid():
#             print(myform.cleaned_data)
#             # Create the model instance with form data
#             review = Review(
#                 user_name=myform.cleaned_data['user_name'],
#                 review_text=myform.cleaned_data['review_text'],
#                 rating=myform.cleaned_data['rating']
#             )
#             review.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         myform = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": myform
#     })


# Use ModelForm features
# There is no need to create a model instance manually
# The ModelForm itself can be saved directly which in
#   turn will populate the associated model and save
#   it to the DB

# def review(request):
#     if request.method == 'POST':
#         # existing_data = Review.objects.get(pk=1)
#         # myform = ReviewForm(request.POST, instance=existing_data)
#         myform = ReviewForm(request.POST)

#         if myform.is_valid():
#             print(myform.cleaned_data)
#             # Create the model instance with form data
#             # review = Review(
#             #     user_name=myform.cleaned_data['user_name'],
#             #     review_text=myform.cleaned_data['review_text'],
#             #     rating=myform.cleaned_data['rating']
#             # )
#             # review.save()
#             myform.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         myform = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": myform
#     })

# Class=based view
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "reviews/review.html", {
            "form": form
        })


def thank_you(request):
    return render(request, "reviews/thank_you.html")