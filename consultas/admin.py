from django.contrib import admin
from .models import Paciente, Medico, Consulta

# Registre seus modelos aqui
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Consulta)
