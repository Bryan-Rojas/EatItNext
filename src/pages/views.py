from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# views.py is where we handle the request/response logic for our web app

class HomePageView(TemplateView):
    template_name = 'home.html'

class BlogView(TemplateView):
    template_name = 'blog.html'

class AboutUsView(TemplateView):
    template_name = 'about-us.html'

class CreditsView(TemplateView):
    template_name = 'credits.html'

class ProjectDocumentView(TemplateView):
    template_name = 'project-docs.html'

class LegalView(TemplateView):
    template_name = 'legal.html'

class TermsOfServiceView(TemplateView):
    template_name = 'tos.html'

class PrivacyPolicyView(TemplateView):
    template_name = 'privacy.html'
    