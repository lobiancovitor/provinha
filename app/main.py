from fastapi import FastAPI

from .controller import calcula_imc

app = FastAPI()

@app.get("/imc/")
def imc(peso: float, altura: float):
    imc = calcula_imc(peso, altura)
    return {"imc": imc}

@app.get("/")
def index():
    return {"data": "ok"}