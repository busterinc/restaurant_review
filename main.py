from fastapi import FastAPI, Body, HTTPException, Depends, Header
from supabase import create_client, Client
# from pydantic import BaseModel, AnyUrl
import os
from dotenv import load_dotenv
from typing import Optional
import uuid
from src import validators

from pydantic import BaseModel, EmailStr

from fastapi.responses import JSONResponse

# from src import verify_token_route
# from src import auth
from src.auth import validate_token, write_token

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales de Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
print('SUPABASE_URL.............', SUPABASE_URL)


# Crear cliente de Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Crear una instancia de FastAPI
app = FastAPI()
app.title = "API - Restaurants Reviews"
app.version = "1.0.0"

# Ruta para obtener Restaurantes de Supabase
@app.get("/api/reviews/restaurant", tags=['RESTAURANT'])
async def get_restaurants(limit: Optional[int] = 10, offset: Optional[int] = 0, token: str = validate_token):

    try:
        response = supabase.table('restaurant').select('*').range(offset, offset + limit - 1).execute()
        print('response ::::::::::::::::', response)
    except Exception as e:
        print('error ::::::::::::::::', e)
        response = str(e)
    
    return response

# Ruta para insertar Restaurante en Supabase
@app.post("/api/reviews/restaurant", tags=['RESTAURANT'])
async def add_restaurant(name: str = Body(), url: str = Body(), image: str = Body()):

    if (name and url and image):
        isImage = validators.validate_image_url(image)
        print('isImage.................', isImage)
        isUrl = validators.validate_url(url)
        print('isUrl.................', isUrl)

        if (isImage and isUrl):
            try:
                isName = supabase.table('restaurant').select('*').eq('name', name).execute()
                print('isName ::::::::::::::::', isName)
                print('isName.data[0] ::::::::::::::::', isName.data[0])
                if isName.data[0]: response = "Ya existe un restaurante con ese nombre"
                else: response = supabase.table('restaurant').insert({"name": name, "url": url, "image": image}).execute()
                print('response ::::::::::::::::', response)
            except Exception as e:
                print('error ::::::::::::::::', e)
                response = str(e)
        elif isImage == False: return "La URL de la imagen no cumple con el formato correcto"
        elif isUrl == False: return "La URL no cumple con el formato correcto"
    else:
        return "Falta ingresar alguno de los campos"
    return response.data

# Ruta para obtener Un Restaurante por Slug de Supabase
@app.get("/api/reviews/restaurant/{slug}", tags=['RESTAURANT'])
async def get_restaurant_slug(slug: str):
    slug_uuid = uuid.UUID(slug)

    try:
        response = supabase.table('restaurant').select('*').eq('slug', slug_uuid).execute()
        print('response ::::::::::::::::', response)

        if len(response.data) == 0:
            return {"message": "Restaurant not found with the provided slug."}

        return response.data[0] 
    except Exception as e:
        print('error ::::::::::::::::', e)
        response = str(e)
    
    return response

# Ruta para actualizar Un Restaurante por Slug de Supabase
@app.put("/api/reviews/restaurant/{slug}", tags=['RESTAURANT'])
async def put_restaurant_slug(slug: str, name: str = Body(), url: str = Body(), image: str = Body()):
    slug_uuid = uuid.UUID(slug)

    try:
        isImage = validators.validate_image_url(image)
        print('isImage.................', isImage)
        isUrl = validators.validate_url(url)
        print('isUrl.................', isUrl)

        if (isImage and isUrl):
            try:
                response = supabase.table('restaurant').update({
                    "name": name,
                    "url": url,
                    "image": image
                }).eq('slug', slug_uuid).execute()
                print('response ::::::::::::::::', response)
            except Exception as e:
                print('error ::::::::::::::::', e)
                response = str(e)
        elif isImage == False: return "La URL de la imagen no cumple con el formato correcto"
        elif isUrl == False: return "La URL no cumple con el formato correcto"

        if len(response.data) == 0:
            return {"message": "Restaurant not found with the provided slug."}

        return response.data[0] 
    except Exception as e:
        print('error ::::::::::::::::', e)
        response = str(e)
    
    return response

# Ruta para patch Un Restaurante por Slug de Supabase
@app.patch("/api/reviews/restaurant/{slug}", tags=['RESTAURANT'])
async def patch_restaurant_slug(slug: str, name: str = Body(None), url: str = Body(None), image: str = Body(None)):
    slug_uuid = uuid.UUID(slug)
    
    update_data = {}
    if name:
        update_data["name"] = name
    if url:
        isUrl = validators.validate_url(url)
        print('isUrl.................', isUrl)
        if not isUrl:  # Si la URL no es válida, se lanza una excepción.
            raise HTTPException(status_code=400, detail="La URL no tiene el formato correcto")
        else: update_data["url"] = url
    if image:
        isImage = validators.validate_image_url(image)
        print('isImage.................', isImage)
        if not isImage:  # Si la imagen no es válida, se lanza una excepción.
            raise HTTPException(status_code=400, detail="La imagen no tiene el formato correcto")
        else: update_data["image"] = image

    # Si no hay datos para actualizar, lanzar un error
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    if (update_data):
        try:
            response = supabase.table('restaurant').update(update_data).eq('slug', slug_uuid).execute()
            print('response ::::::::::::::::', response)

            if len(response.data) == 0:
                return {"message": "Restaurant not found with the provided slug."}

            return response.data[0] 
        except Exception as e:
            print('error ::::::::::::::::', e)
            response = str(e)
    elif isImage == False: return "La URL de la imagen no cumple con el formato correcto"
    elif isUrl == False: return "La URL no cumple con el formato correcto"

    return response

# Ruta para obtener Un Restaurante por Slug de Supabase
@app.delete("/api/reviews/restaurant/{slug}", tags=['RESTAURANT'])
async def delete_restaurant_slug(slug: str):
    slug_uuid = uuid.UUID(slug)

    try:
        response = supabase.table('restaurant').delete().eq('slug', slug_uuid).execute()
        print('response ::::::::::::::::', response)

        if len(response.data) == 0:
            return {"message": "Restaurant not found with the provided slug."}

        return response.data[0] 
    except Exception as e:
        print('error ::::::::::::::::', e)
        response = str(e)
    
    return response



# :::::::::::::::::::::::::::::::: REVIEWS :::::::::::::::::::::::::::::

# Ruta para obtener Restaurantes de Supabase
@app.get("/api/reviews/review", tags=['REVIEWS'])
async def get_reviews(limit: Optional[int] = 10, offset: Optional[int] = 0, token: str = validate_token):

    try:
        response = supabase.table('reviews').select('*').range(offset, offset + limit - 1).execute()
        print('response ::::::::::::::::', response)
    except Exception as e:
        print('error ::::::::::::::::', e)
        response = str(e)
    
    return response

# Ruta para insertar Reviews en Supabase
@app.post("/api/reviews/review", tags=['REVIEWS'])
async def add_review(restaurant: str = Body(), name: str = Body(), description: str = Body(), rating: int = Body()):
    try:
        if (rating < 0):
            return "El rating debe ser mayor que 0"
        elif (rating > 5):
            return "El rating no debe ser menor a 5"
        elif len(restaurant) != 36:
            return "El ID de restaurante no coincide con el formato correcto"
        else:
            isName = supabase.table('reviews').select('*').eq('name', name).execute()
            print('isName ::::::::::::::::', isName)
            print('isName.data[0] ::::::::::::::::', isName.data[0])
            if isName.data[0]: response = "Ya existe un reviews con ese nombre"
            else: response = supabase.table('reviews').insert({"restaurant": restaurant, "name": name, "description": description, "rating": rating}).execute()
            # print('response ::::::::::::::::', response)
    except Exception as e:
        print('error ::::::::::::::::', e)
        response = str(e)

    return response.data


# Ruta para obtener Un Review de Supabase
@app.get("/api/reviews/review/{slug}", tags=['REVIEWS'])
async def get_review_slug(slug: str):
    slug_uuid = uuid.UUID(slug)

    try:
        response = supabase.table('reviews').select('*').eq('key', slug_uuid).execute()
        print('response ::::::::::::::::', response)

        if len(response.data) == 0:
            return {"message": "Restaurant not found with the provided slug."}

        return response.data[0] 
    except Exception as e:
        print('error ::::::::::::::::', e)
        response = str(e)
    
    return response


# Ruta para actualizar Un review por Slug de Supabase
@app.put("/api/reviews/review/{slug}", tags=['REVIEWS'])
async def put_review_slug(slug: str, restaurant: str = Body(), name: str = Body(), description: str = Body(), rating: int = Body()):
    slug_uuid = uuid.UUID(slug)

    try:
        if (rating < 0):
            return "El rating debe ser mayor que 0"
        elif (rating > 5):
            return "El rating no debe ser menor a 5"
        elif len(restaurant) != 36:
            return "El ID de restaurante no coincide con el formato correcto"
        else:
            try:
                response = supabase.table('reviews').update({
                    "restaurant": restaurant,
                    "name": name,
                    "description": description,
                    "rating": rating
                }).eq('key', slug_uuid).execute()
                print('response ::::::::::::::::', response)
            except Exception as e:
                print('error ::::::::::::::::', e)
                response = str(e)

        if len(response.data) == 0:
            return {"message": "Review not found with the provided slug."}

        return response.data[0] 
    except Exception as e:
        print('error ::::::::::::::::', e)
        response = str(e)
    
    return response

# Ruta para patch Un review por Slug de Supabase
@app.patch("/api/reviews/review/{slug}", tags=['REVIEWS'])
async def patch_review_slug(slug: str, restaurant: str = Body(None), name: str = Body(None), description: str = Body(None), rating: int = Body(None)):
    slug_uuid = uuid.UUID(slug)
    
    update_data = {}
    if restaurant:
        if len(restaurant) != 36: return "El ID de restaurante no coincide con el formato correcto"
        else: update_data["restaurant"] = restaurant
    if name:
        update_data["name"] = name
    if description:
        update_data["description"] = description
    if rating:
        if (rating < 0): return "El rating debe ser mayor que 0"
        elif (rating > 5): return "El rating no debe ser menor a 5"
        else: update_data["rating"] = rating

    # Si no hay datos para actualizar, lanzar un error
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    if (update_data):
        try:
            response = supabase.table('reviews').update(update_data).eq('key', slug_uuid).execute()
            print('response ::::::::::::::::', response)

            if len(response.data) == 0:
                return {"message": "Review not found with the provided slug."}

            return response.data[0] 
        except Exception as e:
            print('error ::::::::::::::::', e)
            response = str(e)

    return response

# Ruta para obtener Un review por Slug de Supabase
@app.delete("/api/reviews/review/{slug}", tags=['REVIEWS'])
async def delete_review_slug(slug: str):
    slug_uuid = uuid.UUID(slug)

    try:
        response = supabase.table('reviews').delete().eq('key', slug_uuid).execute()
        print('response ::::::::::::::::', response)

        if len(response.data) == 0:
            return {"message": "Review not found with the provided slug."}

        return response.data[0] 
    except Exception as e:
        print('error ::::::::::::::::', e)
        response = str(e)
    
    return response

# ::::::::::::::::::::::::::::::::::::::::::::: TOKEN :::::::::::::::::::::::::::::::::::::::
# Ruta de login que devuelve un token JWT
class User(BaseModel):
    username: str
    email: EmailStr

@app.post("/login", tags=['TOKEN'])
def login(user: User):
    print(user.dict())

    user_name = os.getenv("USER_NAME")
    user_email = os.getenv("USER_EMAIL")

    if user.username == user_name and user.email == user_email:
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)


@app.post("/verify/token", tags=['TOKEN'])
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)
    
