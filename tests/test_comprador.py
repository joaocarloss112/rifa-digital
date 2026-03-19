import pytest
from src.comprador import criar_numero
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
    sucesso = comprar_bilhete(resultado, numero_desejado, comprador_nome)

    assert sucesso is True
    assert numero_desejado not in rifa_pc["numeros_disponiveis"]
    assert rifa_pc["compradores"][numero_desejado] == "Carlos"
    assert len(rifa_pc["numeros_disponiveis"]) == 19