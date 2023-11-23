from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer
from .tasks import send_welcome_email


class UserCreateView(generics.CreateAPIView):
    """
    With a POST request, сreates a user and sends him a welcome email
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.id)
