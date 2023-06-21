import json

dados = """{
    "nome": "Euller",
    "idade": 18,
    "address": {
        "rua": "Um",
        "num": 9
    }
}
"""

transf = json.loads(dados)

print(transf)

convercao = json.dumps(transf)

print("\n\n", convercao)


