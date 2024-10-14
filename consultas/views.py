from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Paciente, Medico, Consulta
from .forms import PacienteForm, MedicoRegistrationForm, AgendamentoConsultaForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from django.contrib.auth import views as auth_views
from datetime import date


@login_required
def cadastro_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cadastro_paciente")
    else:
        form = PacienteForm()
    return render(request, "consultas/cadastro_paciente.html", {"form": form})


@login_required
def cadastro_medico(request):
    if request.method == "POST":
        form = MedicoRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = MedicoRegistrationForm()
    return render(request, "consultas/cadastro_medico.html", {"form": form})


@login_required
def agendar_consulta(request):
    if request.method == "POST":
        form = AgendamentoConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_consultas")
    else:
        form = AgendamentoConsultaForm()
    return render(request, "consultas/agendamento_consulta.html", {"form": form})


@login_required
def listar_horarios(request, medico_id):
    medico = get_object_or_404(Medico, pk=medico_id)
    data_str = request.GET.get("data")
    data = date.today() if data_str is None else date.fromisoformat(data_str)
    horarios = medico.horarios_disponiveis(data)
    return render(
        request,
        "consultas/listar_horarios.html",
        {"medico": medico, "horarios": horarios, "data": data},
    )


@login_required
def listar_consultas(request):
    consultas = Consulta.objects.filter(medico__user=request.user)
    return render(request, "consultas/listar_consultas.html", {"consultas": consultas})


@login_required
def relatorio_consultas(request):
    consultas = Consulta.objects.all()
    total_consultas = consultas.count()
    return render(
        request,
        "consultas/relatorio_consultas.html",
        {"consultas": consultas, "total_consultas": total_consultas},
    )


def relatorio_consultas_json(request):
    consultas = Consulta.objects.all()
    relatorio = {
        "total_consultas": consultas.count(),
        "consultas_por_medico": {},
    }

    for consulta in consultas:
        medico_nome = consulta.medico.nome
        if medico_nome not in relatorio["consultas_por_medico"]:
            relatorio["consultas_por_medico"][medico_nome] = 0
        relatorio["consultas_por_medico"][medico_nome] += 1

    return JsonResponse(relatorio)


def relatorio_pdf(request):
    consultas = Consulta.objects.all()
    html_string = render_to_string("relatorio.html", {"consultas": consultas})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="relatorio.pdf"'
    HTML(string=html_string).write_pdf(response)
    return response


def registrar_medico(request):
    if request.method == "POST":
        form = MedicoRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = MedicoRegistrationForm()
    return render(request, "consultas/registrar_medico.html", {"form": form})


@login_required
def home(request):
    return render(request, "consultas/home.html")
