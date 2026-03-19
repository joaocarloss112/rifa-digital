import pytest
from src.criar_rifa import verificar_criacao

def test_verificar_criacao():
    nome = "Rifa de PC"
    descricao = "Um PC Gamer"
    qtd = "20"
    preco = "50"
    data = "24/01/2002"
    resultado = verificar_criacao(nome, descricao, qtd, preco, data)

    assert resultado["nome"] == "Rifa de PC"
    assert resultado["quantidade"] == 20  
    assert resultado["preco"] == 50
    assert resultado["descricao"] == "Um PC Gamer"
    assert resultado["data"] == "24/01/2002"