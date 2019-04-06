from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class MealPlanForm(forms.Form):
    diet_prefs_options = (
        ('Any', 'any'),
        ('Vegan', 'vegan'),
        ('Vegetarian', 'vegetarian'),
        ('Paleo', 'paleo'),
        ('Miditerranean', 'miditerranean'),
        ('Ketogenic', 'ketogenic'),
    )
    diet = forms.ChoiceField(choices = diet_prefs_options)
    calories = forms.IntegerField(
        validators = [
            MaxValueValidator(5000),
            MinValueValidator(1200)
        ]
    )

class CalorieCalcForm(forms.Form):
    genders = (
        ('Female', 'female'),
        ('Male', 'male'),
        ('Other', 'other'),
    )
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices = genders)