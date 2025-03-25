# 🍽️ API - Restaurant Reviews

Este proyecto es una API RESTful construida con **FastAPI** y conecta con **Supabase** para gestionar reseñas de restaurantes. Puedes usar esta API para obtener, crear, actualizar y eliminar restaurantes y reseñas asociadas a ellos. La base de datos está alojada en Supabase.

## 📋 Requisitos

- Python 3.7 o superior
- Pip (gestor de dependencias de Python)
- Entorno virtual (recomendado)
- Cuenta de Supabase con las credenciales necesarias (SUPABASE_URL y SUPABASE_KEY)

## 🛠️ Instalación

Sigue estos pasos para instalar las dependencias y configurar el proyecto:

### 1. Clonar el repositorio

```bash
git clone https://github.com/busterinc/restaurant_review
cd restaurants-reviews-api

2. Crear un entorno virtual
Es recomendable usar un entorno virtual para evitar conflictos con otras dependencias de Python. Puedes crear un entorno virtual con el siguiente comando:

En Windows:

python -m venv venv
En Linux/Mac:

python3 -m venv venv
3. Activar el entorno virtual
En Windows:

venv\Scripts\activate
En Linux/Mac:

source venv/bin/activate
4. Instalar las dependencias
Con el entorno virtual activo, instala las dependencias necesarias con pip:

pip install fastapi
pip install supabase
pip install python-dotenv
pip install uvicorn

pip install -r requirements.txt
5. Configurar las variables de entorno
Crea un archivo .env en el directorio raíz del proyecto para almacenar las credenciales de Supabase de manera segura.

touch .env
Abre el archivo .env y agrega las siguientes variables con tus credenciales de Supabase:
```

## env
SUPABASE_URL=tu_supabase_url
SUPABASE_KEY=tu_supabase_key
Nota: Asegúrate de obtener el SUPABASE_URL y SUPABASE_KEY desde tu panel de control de Supabase.

6. Ejecutar el servidor de desarrollo
Una vez que las dependencias estén instaladas y las variables de entorno configuradas, puedes ejecutar el servidor de desarrollo con Uvicorn:

```bash
uvicorn main:app --reload
```
Esto iniciará el servidor en http://127.0.0.1:8000, y podrás acceder a la API desde allí.

## 🚀 Uso de la API
## 🏙️ Obtener todos los restaurantes
GET /api/reviews/restaurant

Obtén una lista de todos los restaurantes almacenados en Supabase.

## 🍽️ Agregar un restaurante
POST /api/reviews/restaurant

Agrega un nuevo restaurante proporcionando los siguientes parámetros en el cuerpo de la solicitud:

```bash
json
{
    "name": "Nombre del Restaurante",
    "url": "URL del restaurante",
    "image": "URL de la imagen del restaurante"
}
```

## 🍔 Obtener un restaurante por slug
GET /api/reviews/restaurant/{slug}

Obtén los detalles de un restaurante específico por su slug.

## ✏️ Actualizar un restaurante por slug
PUT /api/reviews/restaurant/{slug}

Actualiza los detalles de un restaurante específico, proporcionando los campos que deseas modificar.

## 📝 Agregar una reseña
POST /api/reviews/review

Agrega una nueva reseña para un restaurante con los siguientes parámetros:

```bash
json
{
    "restaurant": "ID del restaurante",
    "name": "Tu nombre",
    "description": "Descripción de la reseña",
    "rating": 4
}
```

## 🏆 Obtener reseñas
GET /api/reviews/review

Obtén una lista de todas las reseñas almacenadas en Supabase.

Actualizar una reseña por slug
PUT /api/reviews/review/{slug}

Actualiza los detalles de una reseña específica, proporcionando los campos que deseas modificar.

Eliminar una reseña por slug
DELETE /api/reviews/review/{slug}

Elimina una reseña específica utilizando el slug.

## 🔧 Desarrollo
Si deseas contribuir al proyecto, sigue estos pasos:

Haz un fork del repositorio.

Crea una nueva rama para tus cambios:
git checkout -b feature/nueva-funcionalidad

Realiza tus cambios y haz commit de los mismos.

Empuja los cambios a tu repositorio.

Crea un pull request en GitHub.

## 🧑‍💻 Licencia
Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

¡Disfruta de la API! 🎉 Si tienes alguna pregunta o problema, no dudes en abrir un issue en GitHub. 😊



