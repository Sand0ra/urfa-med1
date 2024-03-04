from rest_framework import serializers

from apps.main.models import *


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = ('title', 'about_company_slug', 'image', 'description')


class OurExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurExperience
        fields = ('title', 'our_experience_slug', 'image', 'description')


class OurCommandProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurCommandProfession
        fields = ('title', 'our_command_profession_slug', 'description')


class OurCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurCommand
        fields = ('title', 'our_command_slug', 'profession', 'description')


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('title', 'vacancy_slug', 'requirements', 'responsibilities', 'conditions', 'pub_date')
