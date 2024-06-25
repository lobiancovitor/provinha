import pytest
from fastapi.testclient import TestClient

from .controller import calcula_imc
from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"data": "ok"}


@pytest.mark.parametrize("peso, altura, esperado", [
    (48.0, 1.749, "Baixo peso muito grave"), 
    (49.0, 1.749, "Baixo peso grave"),
    (52.0, 1.75, "Baixo peso grave"),
    (50, 1.71, "Baixo peso"), 
    (53, 1.70, "Baixo peso"),
    (54, 1.70, "Peso normal"),
    (72, 1.70, "Peso normal"), 
    (73, 1.70, "Sobrepeso"),
    (86, 1.70, "Sobrepeso"),
    (98, 1.80, "Obesidade grau I"), 
    (113, 1.80, "Obesidade grau I"),
    (114, 1.80, "Obesidade grau II"),
    (129, 1.80, "Obesidade grau II"),
    (130, 1.80, "Obesidade grau III (obesidade mórbida)"),
    
])
def test_imc(peso, altura, esperado):
    response = client.get(f"/imc/?peso={peso}&altura={altura}")
    assert response.status_code == 200
    assert response.json()["imc"] == esperado