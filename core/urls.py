from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from consultas.views import (
    cadastro_paciente,
    cadastro_medico,
    agendar_consulta,
    listar_horarios,
    listar_consultas,
    relatorio_consultas,
    relatorio_consultas_json,
    relatorio_pdf,
    registrar_medico,
    home,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        auth_views.LoginView.as_view(template_name="consultas/login.html"),
        name="login",
    ),
    # path(
    #     "logout/",
    #     auth_views.LogoutView.as_view(template_name="consultas/login.html"),
    #     name="logout",
    # ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="consultas/login.html",
            success_url="/home/",  # Redireciona para home após login
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            next_page="login"  # Redireciona para a página de login após logout
        ),
        name="logout",
    ),
    path("cadastro/paciente/", cadastro_paciente, name="cadastro_paciente"),
    path("cadastro/medico/", cadastro_medico, name="cadastro_medico"),
    path("agendar/consulta/", agendar_consulta, name="agendar_consulta"),
    path("horarios/<int:medico_id>/", listar_horarios, name="listar_horarios"),
    path("consultas/", listar_consultas, name="listar_consultas"),
    path("relatorio/consultas/", relatorio_consultas, name="relatorio_consultas"),
    path(
        "relatorio/consultas/json/",
        relatorio_consultas_json,
        name="relatorio_consultas_json",
    ),
    path("relatorio/pdf/", relatorio_pdf, name="relatorio_pdf"),
    path("registrar/medico/", registrar_medico, name="registrar_medico"),
    # path("login/", auth_views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("home/", home, name="home"),
]
