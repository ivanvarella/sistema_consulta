from django.core.mail import send_mail
from django.utils import timezone
from .models import Consulta
from datetime import timedelta


def enviar_lembrete_consulta(consulta_id):
    consulta = Consulta.objects.get(id=consulta_id)
    send_mail(
        "Lembrete de Consulta",
        f"Olá {consulta.paciente},\\n\\nVocê tem uma consulta agendada com {consulta.medico} em {consulta.data_hora}.\\n\\nAtenciosamente,\\nSistema de Gestão de Consultas",
        "seu_email@gmail.com",  # Substitua pelo seu email
        [consulta.paciente.email],
        fail_silently=False,
    )
