from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.http import JsonResponse

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token_data = serializer.validated_data

        updated_token_data = {
            'access_token': token_data['access'],
            'refresh_token': token_data['refresh'],
        }

        response = JsonResponse(updated_token_data)

        return response

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        authenticate_kwargs.update(**{})

        self.user = None

        # Try to authenticate with email if the user exists
        if User.objects.filter(email=attrs[self.username_field]).exists():
            self.user = authenticate(request=self.context.get('request'),
                                     email=attrs[self.username_field],
                                     password=attrs['password'])

        # If the user is still None, raise an authentication error
        if self.user is None:
            self.fail('no_active_account')

        refresh = self.get_token(self.user)

        data = {}
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer