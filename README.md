# OnlyFlans - Sitio Web para PYME de Pastelería

Sitio web desarrollado con Django para la empresa familiar chilena OnlyFlans, dedicada a la venta de flanes y postres de alta calidad. El sitio permite mostrar los productos al público general y ofrecer productos exclusivos a clientes registrados.

## Descripción

OnlyFlans es una PYME fundada en 2021 en Providencia, Santiago. El objetivo del sitio es mostrar los productos al público general y ofrecer contenido exclusivo a clientes registrados, fidelizando así a los clientes recurrentes.

## Tecnologías usadas

- Python 3
- Django
- Bootstrap (diseño responsive)
- SQLite

## Funcionalidades

- Página de inicio con flanes públicos
- Página de bienvenida con flanes exclusivos para usuarios registrados
- Sistema de login y logout con Django
- Formulario de contacto con validación
- Panel de administración de Django
- Página de promociones
- Navbar dinámico según el estado de autenticación

## Modelos

- **Flan:** nombre, descripción, imagen, slug, visibilidad (público/privado), precio
- **ContactForm:** correo, nombre y mensaje del cliente

## Estructura del proyecto

El proyecto contiene los hitos 1 al 4 desarrollados de forma incremental. La carpeta raíz se llama "Hito 1" porque en un inicio no se sabía que los hitos eran incrementales, pero contiene el desarrollo completo.

## Instalación

1. Clonar el repositorio
2. Crear y activar un entorno virtual
3. Instalar dependencias con pip install -r requirements.txt
4. Ejecutar migraciones con python manage.py migrate
5. Levantar el servidor con python manage.py runserver

## Autor

Edgard Andrés Ugarte Pavez
Desarrollo de Aplicaciones Fullstack Python Trainee