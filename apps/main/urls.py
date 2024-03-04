from django.urls import path
from apps.main.views import *


urlpatterns = [
    path('about_company/', AboutCompanyAPI.as_view(), name='api_about_company'),
    path('experience/', OurExperienceAPI.as_view(), name='api_experience'),
    path('our_command_profession/', OurCommandProfessionAPI.as_view(), name='api_our_command_profession'),
    path('our_command/', OurCommandAPI.as_view(), name='api_our_command'),
    path('vacancy/', VacancyAPI.as_view(), name='api_vacancy')
]


