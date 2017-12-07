from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from daas.serializers import UserSerializer


class RegisterAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class ProfileAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return JsonResponse(data=UserSerializer(instance=request.user).data, status=201)