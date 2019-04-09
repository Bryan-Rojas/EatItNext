from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class MealPlanForm(forms.Form):
    diet_prefs_options = (
        ('Any', 'Any'),
        ('Vegan', 'Vegan'),
        ('Vegetarian', 'Vegetarian'),
        ('Paleo', 'Paleo'),
        ('Miditerranean', 'Miditerranean'),
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
        ('Little/No Exericse', 'Little/No Exericse'),
        ('3-5 Times/Week', '3-5 Times/Week'),
        ('Daily Exercise', 'Daily Exercise'),
        ('Intense Daily Exercise', 'Intense Daily Exercise'),
    )

    age = forms.IntegerField()
    gender = forms.ChoiceField(choices = genders)
    current_weight = forms.IntegerField()
    height_ft = forms.IntegerField()
    height_inches = forms.IntegerField()
    exercise_level = forms.ChoiceField(choices = exercise_levels)