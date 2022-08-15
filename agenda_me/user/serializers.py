from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user: User = self.user

        token = self.get_token(self.user)

        # Add custom fields to serialize
        data['access'] = str(token.access_token)
        data['refresh'] = str(token)
        data['company'] = str(user.company)


        return data