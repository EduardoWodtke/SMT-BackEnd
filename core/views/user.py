from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.serializers import PerfilSerializer, TrabalhadorPequeno, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tipo"]

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Return the current authenticated user"""
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TrabalhadorPequeno
        return UserSerializer


class PerfilViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = PerfilSerializer
