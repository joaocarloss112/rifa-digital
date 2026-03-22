from src.criar_rifa import verificar_criacao
from src.comprador import reservar_numero
from src.gerenciamento import confirmar_pagamento, realizar_sorteio
import pytest


def test_pagamento():
    rifa = verificar_criacao("Rifa", "Teste", "5", "10", "01/01/2025")

    reservar_numero(rifa, 1, "Igor", "999")
    assert confirmar_pagamento(rifa, 1) is True
    assert rifa["numeros"][1]["status"] == "vendido"


def test_sorteio():
    rifa = verificar_criacao("Rifa", "Teste", "3", "10", "01/01/2025")

    for i in range(1, 4):
        reservar_numero(rifa, i, "Igor", "999")
        confirmar_pagamento(rifa, i)

    vencedor, dados = realizar_sorteio(rifa)

    assert vencedor in [1, 2, 3]
    assert dados["nome"] == "Igor"


def test_sorteio_incompleto():
    rifa = verificar_criacao("Rifa", "Teste", "3", "10", "01/01/2025")

    reservar_numero(rifa, 1, "Igor", "999")
    confirmar_pagamento(rifa, 1)

    with pytest.raises(ValueError):
        realizar_sorteio(rifa)


def test_pagamento_sem_reserva():
    rifa = verificar_criacao("Rifa", "Teste", "5", "10", "01/01/2025")

    sucesso = confirmar_pagamento(rifa, 1)

    assert sucesso is False