import pytest

from Ex_3 import calcular_frete, calcular_multiplicador_peso, calcular_preco_volume, calcular_multiplicador_rota
from Ex_3 import ler_dimensoes_objeto, validar_medida, ler_peso_objeto, ler_rota


@pytest.fixture()
def colocando_valores_nos_inputs(mocker):
    inputs = mocker.patch("builtins.input")
    inputs.side_effect = [10, 10, 5, 5.0, "br"]
    return inputs


def test_calcular_preco_volume(colocando_valores_nos_inputs):
    valor_do_volume = ler_dimensoes_objeto()
    assert valor_do_volume == 10


def test_validar_medida(colocando_valores_nos_inputs):
    medidas_validadas = [validar_medida(m) for m in [10, 15, 20]]
    # print(medidas_validadas)
    assert all(m != -1 for m in medidas_validadas)


def test_peso_objeto(colocando_valores_nos_inputs):
    peso_objeto = [ler_peso_objeto() for _ in range(3)]
    # print(peso_objeto)
    assert all(p != -1 for p in peso_objeto)


def test_calcular_mult_peso(colocando_valores_nos_inputs):
    peso_obj = [calcular_multiplicador_peso(peso) for peso in [10, 15, 20]]
    # print(peso_obj)
    assert all(p != 0 for p in peso_obj)


@pytest.fixture()
def rotas_para_ler_rota(mocker):
    input_rota = mocker.patch("builtins.input")
    input_rota.side_effect = ["Br"]
    return input_rota


def test_ler_rota(rotas_para_ler_rota):
    lendo_rota = ler_rota()
    # print(lendo_rota)
    assert lendo_rota != -1


def test_calcular_multiplicador_rota(rotas_para_ler_rota):
    calc_mult_rota = ler_rota()
    # print(calc_mult_rota)
    assert 0.0 < calc_mult_rota <= 1.5


def test_calcular_frete(colocando_valores_nos_inputs):
    volume = calcular_preco_volume(volume=1500)
    print(volume)
    multi_peso = calcular_multiplicador_peso(peso=20)
    print(multi_peso)
    multi_rota = calcular_multiplicador_rota(rota="br")
    print(multi_rota)
    frete_calculado = volume * multi_peso * multi_rota
    print(frete_calculado)
    assert frete_calculado == 90.0


def test_calcular_total():
    total = calcular_frete(volume=10, mult_peso=3.0, mult_rota=1.5)
    assert total == 45
