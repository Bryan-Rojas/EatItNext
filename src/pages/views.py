from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import MealPlanForm
# Create your views here.
# views.py is where we handle the request/response logic for our web app

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = MealPlanForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MealPlanForm(request.POST)
        if form.is_valid():
            diet = form.cleaned_data['diet']
            calories = form.cleaned_data['calories']

        args = {
            'form': form,
            'diet': diet,
            'cal': calories
        }

        return render(request, ResultView.template_name, args)

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
    
class CalorieCalcView(TemplateView):
    template_name = 'calorie.html'

class ResultView(TemplateView):
    template_name = 'result.html'
