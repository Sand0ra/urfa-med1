from rest_framework.generics import ListAPIView

from .serializers import *
from .models import *


class RegionApiViews(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = 'region_slug'


class AnalysisApiViews(ListAPIView):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer
    lookup_field = 'analysis_slug'


class AnalysisСategoryApiViews(ListAPIView):
    queryset = AnalysisCategory.objects.all()
    serializer_class = AnalysisСategorySerializer
    lookup_field = 'analysis_category_slug'


class RehabilitationCategoryApiViews(ListAPIView):
    queryset = RehabilitationCategory.objects.all()
    serializer_class = RehabilitationCategorySerializer
    lookup_field = 'rehabilitation_category_slug'


class RehabilitationApiViews(ListAPIView):
    queryset = Rehabilitation.objects.all()
    serializer_class = RehabilitationSerializer
    lookup_field = 'rehabilitation_slug'


class DiagnosticCategoryApiViews(ListAPIView):
    queryset = DiagnosticCategory.objects.all()
    serializer_class = DiagnosticCategorySerializer
    lookup_field = 'diagnostic_category_slug'


class DiagnosticSubcategoryApiViews(ListAPIView):
    queryset = DiagnosticSubcategory.objects.all()
    serializer_class = DiagnosticSubcategorySerializer
    lookup_field = 'diagnostic_subcategory_name'


class DiagnosticApiViews(ListAPIView):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer
    lookup_field = 'diagnostic_slug'


class PolyclinicCategoryApiViews(ListAPIView):
    queryset = PolyclinicCategory.objects.all()
    serializer_class = PolyclinicCategorySerializer
    lookup_field = 'polyclinic_category_slug'


class PolyclinicApiViews(ListAPIView):
    queryset = Polyclinic.objects.all()
    serializer_class = PolyclinicSerializer
    lookup_field = 'polyclinic_slug'


class AddressCenterApiViews(ListAPIView):
    queryset = AddressCenter.objects.all()
    serializer_class = AddressCenterSerializer
    lookup_field = 'address_center_slug'

