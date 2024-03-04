from rest_framework.generics import ListAPIView

from apps.main.models import *
from apps.main.serializers import AboutCompanySerializer, OurExperienceSerializer, OurCommandProfessionSerializer, \
    OurCommandSerializer, VacancySerializer


class AboutCompanyAPI(ListAPIView):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializer
    lookup_field = 'about_company_slug'


class OurExperienceAPI(ListAPIView):
    queryset = OurExperience.objects.all()
    serializer_class = OurExperienceSerializer
    lookup_field = 'our_experience_slug'


class OurCommandProfessionAPI(ListAPIView):
    queryset = OurCommandProfession.objects.all()
    serializer_class = OurCommandProfessionSerializer
    lookup_field = 'our_command_profession_slug'


class OurCommandAPI(ListAPIView):
    queryset = OurCommand.objects.all()
    serializer_class = OurCommandSerializer
    lookup_field = 'our_command_slug'


class VacancyAPI(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    lookup_field = 'vacancy_slug'
