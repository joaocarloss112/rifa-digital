def comprar_numero(rifa, numero, nome_comprador):
    if numero not in rifa["numeros"]:
        return False

    if rifa["numeros"][numero]["status"] != "disponivel":
        return False

    rifa["numeros"][numero] = {
        "status": "vendido",
        "comprador": {
            "nome": nome_comprador
        }
    }

    # compatibilidade
    if numero in rifa["numeros_disponiveis"]:
        rifa["numeros_disponiveis"].remove(numero)
        rifa["compradores"][numero] = nome_comprador

    return True

def reservar_numero(rifa, numero, nome, telefone, email=None):
    if numero not in rifa["numeros"]:
        return False

    if rifa["numeros"][numero]["status"] != "disponivel":
        return False

    rifa["numeros"][numero] = {
        "status": "reservado",
        "comprador": {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }
    }

    if numero in rifa["numeros_disponiveis"]:
        rifa["numeros_disponiveis"].remove(numero)
        rifa["compradores"][numero] = nome

    return True