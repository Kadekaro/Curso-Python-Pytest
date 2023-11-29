from Ex_4 import *


def test_gerar_codigo():
    codigo = gerar_codigo()
    if codigo == 1:
        assert gerar_codigo() == 1
    else:
        assert gerar_codigo() > 1


def test_cadastrar_peca():
    lista_de_cadastro = ["Carro", "Mitsubishi", 50000]
    cadastro = cadastrar_peca(lista_de_cadastro, input_fn=input, print_fn=print)
    assert cadastro == 'Peça Adicionada!'


def test_imprimir_peca(capsys):
    peca_exemplo = {"codigo": 2, "fabricante": "Toyota", "valor": 150000}

    imprimir_peca(peca_exemplo)

    saida_capturada = capsys.readouterr()

    assert "Código: 002" in saida_capturada.out
    assert "Fabricante: Toyota" in saida_capturada.out
    assert "Valor: R$150000" in saida_capturada.out


def test_remover_peca(mocker, capsys):
    # Criar uma peça de exemplo e adicionar à lista
    peca_exemplo = {'codigo': 1, 'nome': 'Exemplo', 'fabricante': 'Fabricante', 'valor': 50.0}
    pecas.append(peca_exemplo)

    # Configurar mocker para input
    inputs = mocker.patch("builtins.input")
    inputs.return_value = "1"

    # Chamar a função
    remover_peca(inputs)

    # Verificar a saída capturada
    saida_capturada = capsys.readouterr()
    assert 'Peça removida com sucesso' in saida_capturada.out
