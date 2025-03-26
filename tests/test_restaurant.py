# tests/test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkFuZ2VsIFJvZHJpZ3VleiIsImVtYWlsIjoiYW5nZWwucmNhYUBnbWFpbC5jb20iLCJleHAiOjE3NDMwOTc1MDV9.uvDd9_mrqHYboKSyRfv0Hx2ORJJDUP2EkZrtkeHYl_c"

def test_get_restaurants():
    response = client.get(f"/api/reviews/restaurant?token={TOKEN}")
    print(response.status_code)  # Imprime el código de estado
    print(response.json())
    assert response.status_code == 200
    
    data = response.json().get('data', [])

    if len(data) > 0:
        for restaurant in data:
            assert isinstance(restaurant['id'], int)
            assert isinstance(restaurant['created_at'], str)
            assert isinstance(restaurant['name'], str)
            assert isinstance(restaurant['url'], str)
            assert isinstance(restaurant['image'], str)
    

def test_get_restaurants_offset_limmit():
    response = client.get(f"/api/reviews/restaurant?limit=10&offset=1&token={TOKEN}")
    print(response.status_code)  # Imprime el código de estado
    print(response.json())
    assert response.status_code == 200
    data = response.json().get('data', [])
    
    # Comprobar que cada restaurante tiene un id numérico
    if len(data) > 0:
        for restaurant in data:
            assert isinstance(restaurant['id'], int)
            assert isinstance(restaurant['created_at'], str)
            assert isinstance(restaurant['name'], str)
            assert isinstance(restaurant['url'], str)
            assert isinstance(restaurant['image'], str)



def test_get_reviews():
    response = client.get(f"/api/reviews/review?token={TOKEN}")
    print(response.status_code)  # Imprime el código de estado
    print(response.json())
    assert response.status_code == 200
    
    data = response.json().get('data', [])

    if len(data) > 0:
        for restaurant in data:
            assert isinstance(restaurant['id'], int)
            assert isinstance(restaurant['created_at'], str)
            assert isinstance(restaurant['name'], str)
            assert isinstance(restaurant['url'], str)
            assert isinstance(restaurant['image'], str)
    

def test_get_reviews_offset_limmit():
    response = client.get(f"/api/reviews/review?limit=10&offset=1&token={TOKEN}")
    print(response.status_code)  # Imprime el código de estado
    print(response.json())
    assert response.status_code == 200
    data = response.json().get('data', [])
    
    # Comprobar que cada restaurante tiene un id numérico
    if len(data) > 0:
        for restaurant in data:
            assert isinstance(restaurant['id'], int)
            assert isinstance(restaurant['created_at'], str)
            assert isinstance(restaurant['name'], str)
            assert isinstance(restaurant['url'], str)
            assert isinstance(restaurant['image'], str)