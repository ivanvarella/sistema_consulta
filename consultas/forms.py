from django import forms
from django.contrib.auth.models import User
from .models import Paciente, Medico, Consulta


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ["nome", "data_nascimento", "telefone", "endereco", "email"]


class MedicoRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            Medico.objects.create(user=user)
        return user


class AgendamentoConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ["paciente", "medico", "data_hora", "observacoes"]
        widgets = {
            "data_hora": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
        }
