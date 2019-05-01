from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('legal/', LegalView.as_view(), name='legal'),
    path('terms-of-service/', TermsOfServiceView.as_view(), name='tos'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('credits/', CreditsView.as_view(), name='credits'),
    path('calorie-calc/', CalorieCalcView.as_view(), name='calorie-calc'),
 ]