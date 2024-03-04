from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm
from .models import UserProfile

from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.

# Helper function to write the uploaded file
def store_file(fileobj):
    with open("temp/image.jpg", "wb+") as destination:
        for chunk in fileobj.chunks():
            destination.write(chunk)


# Creating a class-based view

# class CreateProfileView(View):
#     def get(self, request):
#         return render(request, "profiles/create_profile.html")
    
#     def post(self, request):
#         print(request.FILES['image'])
#         store_file(request.FILES['image'])
#         return HttpResponseRedirect("/profiles")


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })
    
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
        
#         print(request.FILES['user_image'])

#         if submitted_form.is_valid():
#             store_file(request.FILES['user_image'])
#             return HttpResponseRedirect("/profiles")
        
#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })


# Use the model for file upload
            
# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })
    
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)

#         print(request.FILES)

#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES['user_image'])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
        
#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })
            

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = '__all__'
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"

