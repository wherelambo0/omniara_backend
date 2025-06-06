from rest_framework import generics, permissions
from users.models import CustomUser
from rest_framework.serializers import ModelSerializer
import logging

logger = logging.getLogger(__name__)

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    

    def perform_create(self, serializer):
        try:
            serializer.save()
            logger.info(f"New user registered: {serializer.validated_data.get('username')}")
        except Exception as e:
            logger.error(f"Error registering user: {e}", exc_info=True)
            raise
