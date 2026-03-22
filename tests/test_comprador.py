import pytest
from src.comprador import comprar_numero, reservar_numero
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

    sucesso = comprar_numero(resultado, numero_desejado, comprador_nome)

    assert sucesso is True
    assert numero_desejado not in resultado["numeros_disponiveis"]
    assert resultado["compradores"][numero_desejado] == "João Carlos"
    assert len(resultado["numeros_disponiveis"]) == 19


def test_reservar_numero():
    rifa = verificar_criacao("Rifa", "Teste", "10", "5", "01/01/2025")

    sucesso = reservar_numero(rifa, 3, "Igor", "99999999")

    assert sucesso is True
    assert rifa["numeros"][3]["status"] == "reservado"


def test_reserva_duplicada():
    rifa = verificar_criacao("Rifa", "Teste", "10", "5", "01/01/2025")

    sucesso1 = reservar_numero(rifa, 5, "Igor", "999")
    sucesso2 = reservar_numero(rifa, 5, "João", "888")

    assert sucesso1 is True
    assert sucesso2 is False
    assert rifa["numeros"][5]["comprador"]["nome"] == "Igor"