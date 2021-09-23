import json
import pytest
from app.app import app as flask_app
from app.app import process_input

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(app, client):
    response = client.get('/')
    assert response.status_code == 200
    expected = 'This is a house pricing prediction app'
    assert expected == response.get_data(as_text=True)

def test_process_input():
    data = json.dumps(
        {"features": [[1069e-01, 0.0000e+00, 1.3890e+01, 1.0000e+00, 5.5000e-01, 5.9510e+00, 9.3800e+01, 2.8893e+00, 45.0000e+00, 2.7600e+02, 1.6400e+01, 3.9690e+02, 1.7920e+01]]})
    result = process_input(data)
    assert hasattr(result, '__array__')

def test_predict(app, client):
    data = json.dumps(
        {"features": [[1069e-01, 0.0000e+00, 1.3890e+01, 1.0000e+00, 5.5000e-01, 5.9510e+00, 9.3800e+01, 2.8893e+00, 45.0000e+00, 2.7600e+02, 1.6400e+01, 3.9690e+02, 1.7920e+01]]})
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    expected = {"predicted price": [19.1]}
    assert expected == json.loads(response.get_data())