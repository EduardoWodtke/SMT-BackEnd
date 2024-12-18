from rest_framework.serializers import ModelSerializer

from core.models import Trabalho


class TrabalhoSerializer(ModelSerializer):
    class Meta:
        model = Trabalho
        fields = "__all__"


class HistoricoTrabalhoSerializer(ModelSerializer):
    class Meta:
        model = Trabalho
        fields = ("nome", "DataTermino", "estado")


class TrabalhadorAvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Trabalho
        fields = ("nome", "trabalhadorAvaliacao")


class ClienteAvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Trabalho
        fields = ("nome", "clienteAvaliacao")
