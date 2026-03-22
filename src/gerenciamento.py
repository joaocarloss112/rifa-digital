import random

def confirmar_pagamento(rifa, numero):
    if numero not in rifa["numeros"]:
        return False

    if rifa["numeros"][numero]["status"] != "reservado":
        return False

    rifa["numeros"][numero]["status"] = "vendido"


    if numero in rifa["numeros_disponiveis"]:
        rifa["numeros_disponiveis"].remove(numero)

    comprador = rifa["numeros"][numero]["comprador"]
    if comprador:
        rifa["compradores"][numero] = comprador["nome"]

    return True
    

def realizar_sorteio(rifa):
    numeros_vendidos = [
        num for num, info in rifa["numeros"].items()
        if info["status"] == "vendido"
    ]

    if len(numeros_vendidos) != rifa["quantidade"]:
        raise ValueError("Nem todos os números foram vendidos")

    import random
    vencedor = random.choice(numeros_vendidos)

    return vencedor, rifa["numeros"][vencedor]["comprador"]