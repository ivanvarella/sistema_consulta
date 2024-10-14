from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    email = models.EmailField(blank=True)  # Adicionado campo de e-mail

    def __str__(self):
        return self.nome


class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)
    horarios_disponiveis = models.JSONField()

    def __str__(self):
        return self.user.username

    def horarios_disponiveis(self, data):
        horarios = []
        for hora in range(8, 17):
            horarios.append(data.replace(hour=hora, minute=0))
        return horarios


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Consulta de {self.paciente} com {self.medico} em {self.data_hora}"
