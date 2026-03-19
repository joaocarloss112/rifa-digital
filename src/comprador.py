def comprar_numero(rifa, numero, nome_comprador):
    if numero in rifa["numeros_disponiveis"]:
        rifa["numeros_disponiveis"].remove(numero)
        rifa["compradores"][numero] = nome_comprador
        return True
    else:
        return False