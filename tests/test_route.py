from app import app
import re

def test_home_route():
    response = app.hello_world().get('/')
    assert response.status_code == 200
    
def test_colorize_route():
    response = app.colorize().get('/colorize')
    assert response.status_code == 200
    assert response.type == "application/json"
    #assert response.json == ({'result':''} or {'result':{'image': regex "http://*"}})
    
def test_colorize_route():
    response = app.colorize().post('/colorize',data={
        "picture": (resources / "picture.png").open("rb")
    })
    assert response.status_code == 200
    assert response.type == "image/png"
    
def test_results_route():
    response = app.results().get('/results')
    assert response.status_code == 200
    assert response.type == "application/json"
    