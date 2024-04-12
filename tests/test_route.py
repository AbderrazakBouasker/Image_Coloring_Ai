import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
import re

@pytest.fixture
def client():
    with app.test.client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    #response = app.hello_world().get('/')
    assert response.status_code == 200
    
def test_colorize_route(client):
    response = client.post('/colorize', data={
        "image":(open("ressources/picture.png","rb"),"picture.png")
        },follow_redirects=True)
    #response = app.colorize().get('/colorize')
    assert response.status_code == 200
    assert b'colorized_image_url' in response.data
    #assert response.type == "application/json"
    #assert response.json == ({'result':''} or {'result':{'image': regex "http://*"}})
    
def test_colorize_route(client):
    response = client.get('/results')
    #response = app.colorize().post('/colorize',data={
    #    "picture": (resources / "picture.png").open("rb")
    #})
    assert response.status_code == 200
    assert b'images' in response.data
    #assert response.type == "image/png"
    
def test_results_route():
    response = app.results().get('/results')
    assert response.status_code == 200
    assert response.type == "application/json"
    
