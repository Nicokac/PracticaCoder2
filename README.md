# Tercera Pre-Entrega Kachuk

Este es el repositorio del proyecto de la Tercera Pre-Entrega, desarrollado en Django. El proyecto consiste en una aplicación web que permite la gestión de cursos, profesores y estudiantes.


## Instalación

1. Clona el repositorio:
  ```bash
   git clone https://github.com/Nicokac/Tercera_PreEntregaKachuk.git
  ```
  ```bash 
   cd Tercera_PreEntregaKachuk
  ```

  ```bash
  python -m venv env
  source env/bin/activate  # En Mac o Linux
  env\Scripts\activate  # En Windows
  ```

  ```bash
python manage.py migrate
  ```

  ```bash
python manage.py runserver
  ```

Uso
La aplicación permite:

Crear, listar y buscar cursos.
Agregar y gestionar profesores.
Registrar estudiantes.
Puedes navegar por las distintas secciones de la aplicación desde la barra de navegación.

Acceso una vez creado puesto en marcha el servidor
http://127.0.0.1:8000/

Creación de Cursoo
http://127.0.0.1:8000/app-coder/curso-formulario/

Se podrá acceder a un formulario que permite crear nuevos cursos. Se ingresa el nombre y la camada del curso, y luego se presiona "Enviar". Una vez enviado el formulario:

Validación: El formulario verificará que los datos sean correctos. No se permiten nombres vacíos ni valores negativos para la camada.
Creación del Curso: Si los datos son válidos, se creará un nuevo curso con la información proporcionada.
Mensaje de Confirmación: Después de crear el curso, serás redirigido a la pantalla de inicio, donde aparecerá un mensaje confirmando que el curso ha sido creado exitosamente.

Para agregar nuevos profesores a la aplicación:
http://127.0.0.1:8000/app-coder/profesorFormulario/
Este formulario permitirá registrar los datos básicos de un profesor, como su nombre, apellido, correo electrónico, y profesión. Tras completar y enviar el formulario, el profesor se agregará a la base de datos de la aplicación.

Visualización de profesores:
http://127.0.0.1:8000/app-coder/profesores/

Tecnologías Utilizadas
Django 5.1.1: Framework web principal para el desarrollo del proyecto.
Python 3.11.9: Lenguaje de programación usado para desarrollar la aplicación.

Contribuciones
¡Las contribuciones son bienvenidas! Si deseas contribuir, sigue estos pasos:

Realiza un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
Realiza los cambios y haz un commit (git commit -am 'Agregar nueva característica').
Sube la rama (git push origin feature/nueva-caracteristica).
Crea un Pull Request.
