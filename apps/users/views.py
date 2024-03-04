from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import PasswordResetCode
from .serializers import *

from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UserApiViews(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class PatientProfileViews(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = PatientProfileSerializer


class CustomPasswordResetViewSet(CreateAPIView):
    queryset = PasswordResetCode.objects.all()
    serializer_class = CustomPasswordResetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data.get('phone_number')
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Пользователь с таким номером телефона не существует.'}, status=400)

        reset_code = PasswordResetCode.objects.create(user=user)
        reset_code.send_reset_code()

        return JsonResponse({'message': 'Код сброса отправлен успешно.'})


class ResetPasswordViewSet(CreateAPIView):
    queryset = PasswordResetCode.objects.all()
    serializer_class = ResetPasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data.get('phone_number')
        reset_code = serializer.validated_data.get('reset_code')
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Пользователь с таким номером телефона не существует.'}, status=400)

        try:
            code_obj = PasswordResetCode.objects.get(user=user, code=reset_code)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Неверный или просроченный код сброса'}, status=400)

        new_password = serializer.validated_data.get("new_password")
        user.set_password(new_password)
        user.save()
        code_obj.delete()
        return JsonResponse({'message': 'Пароль успешно изменен!'}, status=200)


class TokenLogoutView(ListAPIView):

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Пользователь успешно вышел из системы."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        