from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class MealPlanForm(forms.Form):
    diet_prefs_options = (
        ('Any', 'Any'),
        ('Vegan', 'Vegan'),
        ('Vegetarian', 'Vegetarian'),
        ('Paleo', 'Paleo'),
        ('Ketogenic', 'Ketogenic'),
    )

    diet = forms.ChoiceField(choices = diet_prefs_options)
    calories = forms.IntegerField()

class CalorieCalcForm(forms.Form):
    genders = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    exercise_levels = (
        ('None', 'None'),
        ('Light', 'Light'),
        ('Moderate', 'Moderate'),
        ('Heavy', 'Heavy'),
        ('Extreme', 'Extreme'),
    )
    goals = (
        ('Lose', 'Lose'),
        ('None', 'None'),
        ('Gain', 'Gain'),
        ('Gain Heavily', 'Gain Heavily'),
    )

    age = forms.IntegerField()
    gender = forms.ChoiceField(choices = genders)
    weight = forms.IntegerField()
    height_ft = forms.IntegerField()
    height_in = forms.IntegerField()
    exercise_level = forms.ChoiceField(choices = exercise_levels)
    goal = forms.ChoiceField(choices = goals)