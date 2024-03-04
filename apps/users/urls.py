from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import *


urlpatterns = [
    path('patients/', UserApiViews.as_view(), name='api_patient'),
    path('profile/<int:pk>/', PatientProfileViews.as_view(), name='api_profile'),
    path('custom-password-reset/', CustomPasswordResetViewSet.as_view(), name='api_custom_password_reset'),
    path('reset-password/', ResetPasswordViewSet.as_view(), name='api_reset_password'),
    path('logout/', TokenLogoutView.as_view(), name='logout'),
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('refresh/', TokenRefreshView.as_view(), name='api_refresh'),

]

