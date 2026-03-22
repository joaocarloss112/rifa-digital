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

    return True