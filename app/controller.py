def calcula_imc(peso: float, altura: float) -> str:
    imc = peso / (altura)**2
    
    if imc < 16.0:
      return "Baixo peso muito grave"
    elif imc >= 16.0 and imc <= 16.99:
      return "Baixo peso grave"
    elif imc >= 17.0 and imc <= 18.49:
      return "Baixo peso"
    elif imc >= 18.50 and imc <= 24.99:
      return "Peso normal"
    elif imc >= 25.0 and imc <= 29.99:
      return "Sobrepeso"
    elif imc >= 30.0 and imc <= 34.99:
      return "Obesidade grau I"
    elif imc >= 35.0 and imc <= 39.99:
      return "Obesidade grau II"
    else:
      return "Obesidade grau III (obesidade mórbida)"