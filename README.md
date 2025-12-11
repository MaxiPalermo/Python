# Python
# TuPrimeraPagina+Apellido

Proyecto Django realizado para la tercera entrega del curso.  
El objetivo es crear una web simple utilizando el patrón MVT, con herencia de plantillas, 3 modelos, formularios para carga de datos y un formulario de búsqueda.

---

# Cómo ejecutar el proyecto

# Crear y activar el entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install django

# Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Iniciar el servidor
python manage.py runserver

Abrir en el navegador:  
**http://127.0.0.1:8000/**

---

# Estructura del proyecto

primerapagina/
blog/
migrations/
templates/
home.html
buscar.html
admin.py
models.py
views.py
urls.py
blogproject/
settings.py
urls.py
manage.py

---

# Funcionalidades

# Herencia de plantillas  
Usada para estructurar las páginas (home y búsqueda).

# Modelos (3 clases)
- Autor
- Post
- Comentario

# Formularios de carga de datos  
Realizados mediante el panel de administración de Django:
http://127.0.0.1:8000/admin/

# Formulario de búsqueda  
Disponible en:
http://127.0.0.1:8000/buscar/

Permite buscar posts por título.

---

# Orden para probar la aplicación

1. Entrar al admin:  
   http://127.0.0.1:8000/admin/

2. Cargar:
   - Uno o más autores
   - Posts asociados a autores
   - Comentarios asociados

3. Ver el blog en:  
   http://127.0.0.1:8000/

4. Usar el buscador:  
   http://127.0.0.1:8000/buscar/

---

# Tecnologías usadas
- Python
- Django
- HTML

---

# Entrega final  
Este repositorio cumple con:
- Herencia de plantillas  
- 3 modelos  
- Formularios para cargar datos  
- Formulario de búsqueda  
- Proyecto Django completo  
- README explicativo  
