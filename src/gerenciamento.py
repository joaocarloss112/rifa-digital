import random

def confirmar_pagamento(rifa, numero):
    if numero not in rifa["numeros"]:
        return False

    if rifa["numeros"][numero]["status"] != "reservado":
        return False

    rifa["numeros"][numero]["status"] = "vendido"
    return True


def realizar_sorteio(rifa):
    numeros_vendidos = [
        num for num, info in rifa["numeros"].items()
        if info["status"] == "vendido"
    ]

    if len(numeros_vendidos) != rifa["quantidade"]:
        raise Exception("Nem todos os números foram vendidos")

    vencedor = random.choice(numeros_vendidos)

    return vencedor, rifa["numeros"][vencedor]["comprador"]