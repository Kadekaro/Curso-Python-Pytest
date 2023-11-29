import pytest
from Ex_1.Ex_1 import calcular_valor


def test_calculo_desconto():
    valor_unitario = 100  # Valor unitário fictício para teste
    quantidade = 50  # Quantidade fictícia para teste
    valor_com_desconto = calcular_valor(valor_unitario, quantidade)

    # Verifica se os valores calculados correspondem ao esperado
    assert valor_com_desconto[0] == 4750  # Valor com desconto


def test_calculo_sem_desconto():
    valor_unitario = 100
    quantidade = 50
    valor_sem_desconto = calcular_valor(valor_unitario, quantidade)

    # Verifica se os valores calculados correspondem ao esperado
    assert valor_sem_desconto[1] == 5000  # Valor sem desconto


if __name__ == '__main__':
    pytest.main()
