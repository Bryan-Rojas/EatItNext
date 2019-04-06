from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import MealPlanForm, CalorieCalcForm
from .mealplanner import randomMealPlan
import json

# Create your views here.
# views.py is where we handle the request/response logic for our web app

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = MealPlanForm()
        args = {
            'form': form,
            'null': True,
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = MealPlanForm(request.POST)
        if form.is_valid():
            diet = form.cleaned_data['diet']
            calories = form.cleaned_data['calories']

        args = randomMealPlan(str(diet), int(calories))
        args['form'] = form
        args['null'] = False
        args['diet'] = diet
        args['calories_wanted'] = calories

        return render(request, self.template_name, args)

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

    def get(self, request):
        form = CalorieCalcForm()
        args = {
            'form': form,
            'null': True,
        }

        return render(request, self.template_name, args)