from rest_framework.serializers import CharField, ModelSerializer

from core.models import User


class TrabalhadorPequeno(ModelSerializer):
    class Meta:
        model = User
        fields = ("foto", "name", "categoria", "tipo")
        depth = 1


class UserSerializer(ModelSerializer):
    foto = CharField(source="foto.url", read_only=True)

    class Meta:
        model = User
        fields = "__all__"
        depth = 1


class PerfilSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "foto", "capa", "publicacao", "publicacaoFoto", "descricao")
        depth = 1
