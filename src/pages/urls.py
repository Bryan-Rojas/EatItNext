from django.urls import path
from .views import HomePageView, AboutUsView, MeetTheTeamView, LegalView, TermsOfServiceView, PrivacyPolicyView, CreditsView, CalorieCalcView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('meet-the-team/', MeetTheTeamView.as_view(), name='meet-the-team'),
    path('legal/', LegalView.as_view(), name='legal'),
    path('terms-of-service/', TermsOfServiceView.as_view(), name='tos'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('credits/', CreditsView.as_view(), name='credits'),
    path('calorie-calc/', CalorieCalcView.as_view(), name='calorie-calc'),
 ]