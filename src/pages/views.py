from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import MealPlanForm, CalorieCalcForm
from .mealplanner import randomMealPlan
from .calcalc import calorieCalulator
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
        if calories >= 800 and calories <= 5200:
            args['valid'] = True
        else:
            args['valid'] = False
            args['calories_invalid'] = True

        return render(request, self.template_name, args)

class MeetTheTeamView(TemplateView):
    template_name = 'team.html'

class AboutUsView(TemplateView):
    template_name = 'about-us.html'

class CreditsView(TemplateView):
    template_name = 'credits.html'

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

    def post(self, request):
        form = CalorieCalcForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            weight = form.cleaned_data['weight']
            height_ft = form.cleaned_data['height_ft']
            height_in = form.cleaned_data['height_in']
            exercise_level = form.cleaned_data['exercise_level']
            goal = form.cleaned_data['goal']

        args = {}

        #make function dummie
        if weight >= 20 and weight <= 800:
            args['valid'] = True
            args = calorieCalulator(int(age), str(gender), int(weight), int(height_ft), int(height_in), str(exercise_level), str(goal))
        else:
            args['valid'] = False

        #age, gender, weight, height_ft, height_in, activity_level, goal
        #args = calorieCalulator(int(age), str(gender), int(weight), int(height_ft), int(height_in), str(exercise_level), str(goal))

        args['form'] = form
        args['null'] = False

        return render(request, self.template_name, args)