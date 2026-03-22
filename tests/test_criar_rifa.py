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


def test_geracao_numeros():
    rifa = verificar_criacao("Teste", "Desc", "5", "10", "01/01/2025")

    assert len(rifa["numeros"]) == 5
    assert rifa["numeros"][1]["status"] == "disponivel"

def test_campos_obrigatorios():
    with pytest.raises(ValueError):
        verificar_criacao("", "Desc", "10", "5", "01/01/2025")


def test_limites_numeros():
    rifa = verificar_criacao("Teste", "Desc", "5", "10", "01/01/2025")

    assert 1 in rifa["numeros"]
    assert 5 in rifa["numeros"]


def test_estrutura_rifa():
    rifa = verificar_criacao("Teste", "Desc", "5", "10", "01/01/2025")

    assert "numeros" in rifa
    assert "numeros_disponiveis" in rifa
    assert "compradores" in rifa