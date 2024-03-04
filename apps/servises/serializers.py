from rest_framework import serializers

from .models import *


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('title', 'region_slug')


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ('analysis_name', 'analysis_slug', 'analysis_description', 'price',
                  'Patient_instructions', 'procedure_description', 'expected_results',
                  'results_delivery_time', 'promotion', 'created', 'updated')


class AnalysisСategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisCategory
        fields = ('region', 'category_name', 'analysis_category_slug', 'category_description')


class RehabilitationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RehabilitationCategory
        fields = ('region', 'rehabilitation_category_slug', 'rehabilitation_category_name')


class RehabilitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rehabilitation
        fields = ('rehabilitation_name', 'rehabilitation_slug', 'image', 'rehabilitation_description')


class DiagnosticCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticCategory
        fields = ('region', 'diagnostic_category_slug', 'diagnostic_category_name')


class DiagnosticSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticSubcategory
        fields = ('diagnostic_subcategory_name', 'diagnostic_subcategory_slug', 'diagnostic_subcategory_description',
                  'image')


class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = ('diagnostic_name', 'diagnostic_slug', 'image', 'description',
                  'sale', 'promotion')


class PolyclinicCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PolyclinicCategory
        fields = ('polyclinic_category_name', 'polyclinic_category_slug')


class PolyclinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polyclinic
        fields = ('polyclinic_name', 'polyclinic_slug', 'price_first_meet', 'price_second_meet',
                  'about_service', 'about_procedure')


class AddressCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressCenter
        fields = ('title', 'address_center_slug', 'description')
