<div align="center" style="padding-top: 20px;">
  
# Sistema de Gestão de Consultas Médicas

## Este projeto implementa uma aplicação web construída com Django para gerenciar consultas médicas, focando em agendamento, organização e controle de informações.

</div>


## Índice
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Observações](#observações)
- [Dependências](#dependências)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Documentação](#documentação)
- [Testes](#testes)
- [Contribuição](#contribuição)

## Funcionalidades

- **Cadastro e gerenciamento de pacientes:**
    - Cadastro de novos pacientes com informações completas.
    - Edição de informações de pacientes existentes.
    - Visualização de histórico de consultas do paciente.
- **Cadastro e gerenciamento de médicos:**
    - Cadastro de médicos com especialidades e informações de contato.
    - Edição de informações de médicos cadastrados.
    - Visualização da agenda de consultas do médico.
- **Agendamento de consultas:**
    - Agendamento de consultas com seleção de médico, data e hora.
    -  Integração com sistema de horários disponíveis do médico, evitando conflitos.
    - Confirmação de agendamento e notificações.
- **Sistema de notificações:**
    - Lembretes de consultas por e-mail para pacientes.
    -  Possibilidade de implementar notificações por SMS.
- **Geração de relatórios:**
    - Relatórios de consultas por período, médico ou paciente.
    -  Funcionalidade para exportar relatórios em PDF.
- **Autenticação e autorização:**
    - Sistema de login para médicos e secretárias.
    - Controle de acesso para diferentes tipos de usuários.


## Tecnologias Utilizadas

- ![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
- ![Django](https://img.shields.io/badge/Django-5.x-green.svg)
- ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=plastic&logo=sqlite&logoColor=white) 
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-5-blue.svg)
- ![HTML](https://img.shields.io/badge/HTML5-E34F26.svg?logo=html5&logoColor=white)
- ![CSS](https://img.shields.io/badge/CSS3-1572B6.svg?logo=css3&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)
- ![Git](https://img.shields.io/badge/Git-F05032.svg?logo=git&logoColor=white)
- ![GitHub](https://img.shields.io/badge/GitHub-181717.svg?logo=github&logoColor=white)

## Como Executar o Projeto

1. **Clone o repositório:**  
   ```bash
   git clone https://github.com/ivanvarella/sistema_consulta.git
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados:**
   - Aplique as migrações:
     ```bash
     python manage.py migrate
     ```

5. **Crie um superusuário:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação:**  
    Abra o seu navegador e acesse: http://127.0.0.1:8000/

## Observações

- Este projeto é um exemplo e pode ser expandido com funcionalidades adicionais.
- A segurança e a proteção de dados devem ser cuidadosamente consideradas em um ambiente de produção.
- Adapte o código e as configurações às suas necessidades específicas.

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`.
Para instalar as dependências, execute:

```bash
pip install -r requirements.txt
```

## Estrutura do Repositório

```
sistema-consultas-medicas/
├── consultas/ # Contém os modelos, views, e outros arquivos do app Django
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── ...
├── templates/ # Contém os arquivos de template HTML
│   └── ...
├── static/ # Contém arquivos estáticos como CSS, JavaScript e imagens
│   └── ...
├── sistema_consultas/ # Diretório raiz do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── manage.py
└── requirements.txt
```

## Contribuição

Sinta-se à vontade para contribuir com o projeto! 
Você pode abrir issues, enviar pull requests ou entrar em contato com os desenvolvedores.

<br><br>
<hr>
<div align="center">
  
# 🌐 English Version Below 🌐

</div>

<br><br>

<div align="center" style="padding-top: 20px;">
  
# Medical Appointment Management System

## This project implements a web application built with Django to manage medical appointments, focusing on scheduling, organization, and information control.

</div>


## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How to Run the Project](#how-to-run-the-project)
- [Notes](#notes)
- [Dependencies](#dependencies)
- [Repository Structure](#repository-structure)
- [Documentation](#documentation)
- [Testing](#testing)
- [Contribution](#contribution)

## Features

- **Patient registration and management:**
    - Registration of new patients with complete information.
    - Editing information of existing patients.
    - Viewing patient appointment history.
- **Doctor registration and management:**
    - Registration of doctors with specialties and contact information.
    - Editing information of registered doctors.
    - Viewing the doctor's appointment schedule.
- **Appointment scheduling:**
    - Scheduling appointments with doctor, date, and time selection.
    - Integration with the doctor's available time system, avoiding conflicts.
    - Appointment confirmation and notifications.
- **Notification system:**
    - Email appointment reminders for patients.
    - Ability to implement SMS notifications.
- **Report generation:**
    - Appointment reports by period, doctor, or patient.
    - Functionality to export reports in PDF format.
- **Authentication and authorization:**
    - Login system for doctors and secretaries.
    - Access control for different types of users.


## Technologies Used

- ![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
- ![Django](https://img.shields.io/badge/Django-5.x-green.svg)
- ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=plastic&logo=sqlite&logoColor=white) 
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-5-blue.svg)
- ![HTML](https://img.shields.io/badge/HTML5-E34F26.svg?logo=html5&logoColor=white)
- ![CSS](https://img.shields.io/badge/CSS3-1572B6.svg?logo=css3&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)
- ![Git](https://img.shields.io/badge/Git-F05032.svg?logo=git&logoColor=white)
- ![GitHub](https://img.shields.io/badge/GitHub-181717.svg?logo=github&logoColor=white)

## How to Run the Project

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/ivanvarella/sistema_consulta.git
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - Apply the migrations:
     ```bash
     python manage.py migrate
     ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**  
    Open your browser and go to: http://127.0.0.1:8000/

## Notes

- This project is an example and can be expanded with additional features.
- Data security and protection should be carefully considered in a production environment.
- Adapt the code and settings to your specific needs.

## Dependencies

Project dependencies are listed in the `requirements.txt` file.
To install the dependencies, run:

```bash
pip install -r requirements.txt
```

## Repository Structure

```
medical-appointment-system/
├── appointments/ # Contains models, views, and other files of the Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── ...
├── templates/ # Contains HTML template files
│   └── ...
├── static/ # Contains static files such as CSS, JavaScript, and images
│   └── ...
├── medical_appointments/ # Django project root directory
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── manage.py
└── requirements.txt
```

## Contribution

Feel free to contribute to the project! 
You can open issues, submit pull requests, or get in touch with the developers.