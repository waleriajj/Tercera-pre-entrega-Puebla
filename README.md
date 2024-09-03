# Tercera Pre-Entrega - Puebla

Este proyecto es una aplicación web desarrollada en Django como parte de la tercera pre-entrega del curso. La aplicación sigue el patrón MVT (Model-View-Template) y permite gestionar una biblioteca básica. Se han creado modelos para representar autores, estilos literarios y libros, y se han implementado vistas que permiten la creación, búsqueda y visualización de registros. El proyecto incluye herencia de plantillas HTML y está vinculado a un repositorio en GitHub para control de versiones.

## Funcionalidades principales

- **Modelos**: Definición de modelos para Autor, Estilo y Libro.
- **Vistas**: Implementación de vistas para la página principal y búsqueda de libros.
- **Plantillas HTML**: Uso de herencia de plantillas para estructurar las páginas de la aplicación.
- **GitHub**: Proyecto vinculado y subido a un repositorio en GitHub.

## Cómo ejecutar el proyecto

1. Clona este repositorio.
2. Crea un entorno virtual e instala las dependencias usando `pip install -r requirements.txt`.
3. Ejecuta las migraciones con `python manage.py migrate`.
4. Inicia el servidor de desarrollo con `python manage.py runserver`.
5. Accede a la aplicación en `http://127.0.0.1:8000/libros/`.
