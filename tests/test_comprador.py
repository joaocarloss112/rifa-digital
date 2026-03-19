import pytest
from src.comprador import comprar_numero
from src.criar_rifa import verificar_criacao

def test_compra():
    nome = "Rifa de PC"
    descricao = "Um PC Gamer"
    qtd = "20"
    preco = "50"
    data = "24/01/2002"
    resultado = verificar_criacao(nome, descricao, qtd, preco, data)
    numero_desejado = 7
    comprador_nome = "João Carlos"
    numeros_disponiveis = "20"
    sucesso = comprar_numero(resultado, numero_desejado, comprador_nome)

    assert sucesso is True
    assert numero_desejado not in resultado["numeros_disponiveis"]
    assert resultado["compradores"][numero_desejado] == "João Carlos"
    assert len(resultado["numeros_disponiveis"]) == 19