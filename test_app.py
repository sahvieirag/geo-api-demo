import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_nearby_endpoint_success(client):
    """Testa o endpoint /api/nearby com parâmetros válidos."""
    response = client.get('/api/nearby?origin=google_campus_sp&radius=10')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    # Verifica se São Paulo está nos resultados, já que está próximo ao campus do Google
    found = any(d['name'] == 'sao_paulo_sp' for d in data)
    assert found is True

def test_nearby_endpoint_missing_params(client):
    """Testa o endpoint /api/nearby sem os parâmetros necessários."""
    response = client.get('/api/nearby?origin=google_campus_sp')
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data