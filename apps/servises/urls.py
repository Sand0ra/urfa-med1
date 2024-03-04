from .views import *
from django.urls import path

urlpatterns = [
    path('region/',RegionApiViews.as_view(), name='api_region'),
    path('analysis/',AnalysisApiViews.as_view(), name='api_analysis'),
    path('analysis_subcategory/',AnalysisСategoryApiViews.as_view(), name='api_analysis_category'),
    path('rehabilitation_category/', RehabilitationCategoryApiViews.as_view(), name='api_rehabilitation_category'),
    path('rehabilitation/', RehabilitationApiViews.as_view(), name='api_rehabilitation'),
    path('diagnostic_category/', DiagnosticCategoryApiViews.as_view(), name='api_diagnostic'),
    path('diagnostic_subcategory/', DiagnosticSubcategoryApiViews.as_view(), name='api_diagnostic_category'),
    path('diagnostic/', DiagnosticApiViews.as_view(),name='api_diagnostic' ),
    path('polyclinic_category/', PolyclinicCategoryApiViews.as_view(), name='api_polyclinic_category'),
    path('polyclinic/', PolyclinicApiViews.as_view(), name='api_polyclinic'),
    path('adress_center/', AddressCenterApiViews.as_view(), name='api_adress_center')
]

