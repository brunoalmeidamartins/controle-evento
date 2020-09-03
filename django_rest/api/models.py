from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.nome

class Convidado(models.Model):
    funcionario = models.ForeignKey("Funcionario", on_delete=models.CASCADE)
    nome = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    total_arrecadado = models.FloatField(blank=True)
    total_gasto = models.FloatField(blank=True)
    total_gasto_comida = models.FloatField(blank=True)
    total_gasto_bebida = models.FloatField(blank=True)

    def __str__(self):
        return self.nome

class Evento_Funcionario(models.Model):
    class Meta:
        unique_together = (('evento', 'funcionario'),)
    evento = models.ForeignKey("Evento", on_delete=models.CASCADE)
    funcionario = models.ForeignKey("Funcionario", on_delete=models.CASCADE)
    convidado = models.ForeignKey("Convidado", on_delete=models.CASCADE, null=True)
    funcionario_bebe = models.BooleanField(default=True)
    convidado_bebe = models.BooleanField(default=True)