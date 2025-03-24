from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import HTMLResponse
from typing import Optional


import requests

# from src import catalogVars

app = FastAPI()
app.title = "API - Restaurant El Mirador"
app.version = "1.0.0"

API_URL = "https://depfly-backend.behuns.com/api/reviews"

@app.get('/api/reviews/restauant/', tags=['RESTAURANT'])
async def get_restaurant(limit: Optional[int] = '', offset: Optional[int] = ''):
    headers = {"accept": "application/json"}
    url = f"{API_URL}/restaurant/?limit={limit}&offset={offset}"
    print('url :::::::::::::::::', url)

    try:
        response = requests.get(url, headers=headers)
        result = response.json()
        print('result ::::::::::::::::', result)
    except Exception as e:
        print('error ::::::::::::::::', e)
        result = str(e)

    return result

@app.get('/api/reviews/restauant/{slug}', tags=['RESTAURANT'])
async def get_slugs(slug: str):
    headers = {"accept": "application/json"}
    url = f"{API_URL}/restaurant/{slug}"
    print('url :::::::::::::::::', url)

    try:
        response = requests.get(url, headers=headers)
        result = response.json()
        print('result ::::::::::::::::', result)
    except Exception as e:
        print('error ::::::::::::::::', e)
        result = str(e)

    return result

@app.get('/api/reviews/reviews/', tags=['REVIEWS'])
async def get_reviews(limit: Optional[str]= '', offset: Optional[str]= '', restaurant__slug: Optional[str] = ''):
    headers = {"accept": "application/json"}
    url = f"{API_URL}/review/?limit={limit}&offset={offset}&restaurant__slug={restaurant__slug}"
    print('url :::::::::::::::::', url)

    try:
        response = requests.get(url, headers=headers)
        result = response.json()
        print('result ::::::::::::::::', result)
    except Exception as e:
        print('error ::::::::::::::::', e)
        result = str(e)

    return result


@app.post('/api/reviews/reviews/', tags=['REVIEWS'])
async def post_review(restaurant: str = Body(), name: str = Body(), description: str = Body(), rating: int = Body()):
    # return {"restaurant": restaurant, "name": name, "description": description, "rating": rating}

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    url = f"{API_URL}/review/"
    print('url :::::::::::::::::', url)

    payload = {
        "restaurant": restaurant,
        "name": name,
        "description": description,
        "rating": rating
    }
    try:
        # response = requests.request("POST", url, headers=headers, data=payload)
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        print('result ::::::::::::::::', result)
    except Exception as e:
        print('error ::::::::::::::::', e)
        result = str(e)

    return result

@app.get('/api/reviews/review/{slug}', tags=['REVIEWS'])
async def get_review_slug(slug: str):
    headers = {"accept": "application/json"}
    url = f"{API_URL}/review/{slug}"
    print('url :::::::::::::::::', url)

    try:
        response = requests.get(url, headers=headers)
        result = response.json()
        print('result ::::::::::::::::', result)
    except Exception as e:
        print('error ::::::::::::::::', e)
        result = str(e)

    return result


@app.put('/api/reviews/reviews/{slug}', tags=['REVIEWS'])
async def put_review_slug(slug: str, restaurant: str = Body(), name: str = Body(), description: str = Body(), rating: int = Body()):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    url = f"{API_URL}/review/{slug}/"
    print('url :::::::::::::::::', url)

    payload = {
        "restaurant": restaurant,
        "name": name,
        "description": description,
        "rating": rating
    }
    try:
        # response = requests.request("POST", url, headers=headers, data=payload)
        response = requests.put(url, headers=headers, json=payload)

        if response.status_code == 200:
            # Intentar obtener la respuesta JSON
            result = response.json()
            print('result ::::::::::::::::', result)
        else:
            print(f"Error al hacer la solicitud: {response.status_code}")
            result = {"error": "No se pudo actualizar el recurso", "status_code": response.status_code, "detail": response.text}
    except Exception as e:
        print('error ::::::::::::::::', e)
        result = str(e)

    return result

@app.patch('/api/reviews/reviews/{slug}', tags=['REVIEWS'])
async def patch_review_slug(slug: str, restaurant: str = Body(), name: str = Body(), description: str = Body(), rating: int = Body()):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    url = f"{API_URL}/review/{slug}/"
    print('url :::::::::::::::::', url)

    payload = {
        "restaurant": restaurant,
        "name": name,
        "description": description,
        "rating": rating
    }
    try:
        response = requests.patch(url, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            print('result ::::::::::::::::', result)
        else:
            print(f"Error al hacer la solicitud: {response.status_code}")
            result = {"error": "No se pudo actualizar el recurso", "status_code": response.status_code, "detail": response.text}
    except Exception as e:
        print('error ::::::::::::::::', e)
        result = str(e)

    return result


@app.delete('/api/reviews/review/{slug}', tags=['REVIEWS'])
async def delete_review_slug(slug: str):
    headers = {"accept": "application/json"}
    url = f"{API_URL}/restaurant/{slug}"
    print('url :::::::::::::::::', url)

    try:
        # Realizamos la solicitud DELETE
        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            result = {"message": "Revisión eliminada exitosamente"}
        elif response.status_code == 200:
            result = response.json()
        else:
            result = {"error": "Hubo un problema al eliminar la revisión", "status_code": response.status_code, "detail": response.text}
        
        print('result ::::::::::::::::', result)
        
    except Exception as e:
        print('error ::::::::::::::::', e)
        result = {"error": str(e)}

    return result
