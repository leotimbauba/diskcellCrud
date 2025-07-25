from django.db import models

class Marca(models.Model):
    nome = models.CharField("Marca", max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Modelo(models.Model):
    marca = models.ForeignKey(Marca, related_name="modelos", on_delete=models.CASCADE)
    nome = models.CharField("Modelo", max_length=100)

    class Meta:
        unique_together = ('marca', 'nome')

    def __str__(self):
        return f"{self.marca.nome} {self.nome}"
