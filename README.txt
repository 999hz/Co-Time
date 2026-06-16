🚀 Co-Time | Gestión de Espacios
Co-Time es una plataforma web desarrollada con Django diseñada para optimizar la reserva y administración de espacios comunes en entornos de Coworking. El sistema permite gestionar flujos de usuarios, controlar la disponibilidad en tiempo real y visualizar la actividad diaria mediante una interfaz intuitiva.

📋 Funcionalidades Principales
Autenticación Segura: Login, Logout y manejo de sesiones.

Control de Acceso: Diferenciación entre Superusuarios (administran todo) y Usuarios Finales (gestionan sus propias reservas).

CRUD de Reservas: Crear, listar y cancelar reservas.

Agenda Inteligente: Vista global de actividad con resaltado automático de eventos del día actual.

Contador en Tiempo Real: Visualización dinámica de la ocupación del día en la barra de navegación.

💻 Instalación y Configuración
Sigue estos pasos para levantar el proyecto en tu entorno local:

1. Clonar o descargar el proyecto
Bash
# Si usas git
git clone https://github.com/999hz/Co-Time.git
cd co-time
2. Crear y activar el entorno virtual
Bash
# Crear entorno
python -m venv .venv

# Activar en Windows
.venv\Scripts\activate

# Activar en Mac/Linux
source .venv/bin/activate

3. Instalar dependencias
Asegúrate de tener Django instalado en tu entorno:

# Bash
pip install -r requirements.txt

4.hacer las migraciones

python manage.py makemigrations

python manage.py migrate

5. Iniciar el servidor
Bash
python manage.py runserver
El sitio estará disponible en: http://127.0.0.1:8000/

📂 Estructura del Proyecto
core/: Aplicación encargada de la bienvenida, contacto y estilos globales.

reservas/: Lógica principal de gestión de espacios y formularios.

static/: Archivos CSS personalizados.

templates/: Estructura de herencia HTML (base.html).

🛡️ Credenciales de Prueba:

Admin: admin / admin123

Usuario: Cliente / usuario12345


