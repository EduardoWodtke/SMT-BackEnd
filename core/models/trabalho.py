from django.db import models

from .user import User


class Trabalho(models.Model):

    class Estado(models.IntegerChoices):
        NEGOCIO = 1, "Negocio"
        EM_ANDAMENTO = 2, "Em andamento"
        CONCLUIDO = 3, "Concluido"
        PAGO = 4, "Pago"
        CANCELADO = 5, "Cancelado"

    DataInicio = models.DateField()
    prazo = models.DateField()
    DataTermino = models.DateField(blank=True, null=True)
    preco = models.DecimalField(max_digits=8, decimal_places=1)
    nome = models.CharField(max_length=30)
    estado = models.IntegerField(choices=Estado.choices, default=1)
    trabalhadorAvaliacao = models.DecimalField(max_digits=3, decimal_places=1)
    clienteAvaliacao = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"({self.id}) | nome: {self.nome or ''} | Iniciou-se: {self.DataInicio} | Prazo : {self.prazo} | Terminou em: {self.DataTermino}"
