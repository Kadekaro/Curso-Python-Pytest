from typing import Callable, List

pecas = []


def gerar_codigo():
    tamanho_lista = len(pecas)
    if tamanho_lista > 0:
        ultima_peca = pecas[tamanho_lista - 1]
        ultimo_codigo = ultima_peca['codigo']
        return ultimo_codigo + 1

    return 1


def cadastrar_peca(inputs: List, input_fn: Callable = input, print_fn: Callable = print):
    codigo = gerar_codigo()
    print_fn(f'\nCódigo da peça: {codigo:03d}')
    nome = inputs.pop(0) if inputs else input_fn('Por favor entre com o nome da peça: ')
    fabricante = inputs.pop(0) if inputs else input_fn('Por favor entre com o fabricante da peça: ')
    valor = inputs.pop(0) if inputs else float(input_fn('Por favor entre com o valor da peça (R$): '))
    peca = {
        'codigo': codigo,
        'nome': nome,
        'fabricante': fabricante,
        'valor': valor
    }

    pecas.append(peca)
    print_fn('Peça Adicionada!\n')
    return 'Peça Adicionada!'


def imprimir_peca(peca: dict, print_fn: Callable = print):
    print_fn(f'\nCódigo: {peca["codigo"]:03d}')
    print_fn(f'Fabricante: {peca["fabricante"]}')
    print_fn(f'Valor: R${peca["valor"]:.2f}')
    print_fn()


def consultar_pecas(input_fn: Callable = input, print_fn: Callable = print):
    finaliza_consulta = False
    while not finaliza_consulta:
        print_fn('\nVocê selecionou a opção para consultar peças! ')
        print_fn('Escolha a opção desejada:')
        print_fn('1 - Consultar todas as pecas')
        print_fn('2 - Consultar peças por código')
        print_fn('3 - Consultar peças por fabricante')
        print_fn('4 - Retornar')
        opcao_consulta = obter_opcao_consulta(input_fn)
        print_fn()
        if opcao_consulta == 1:
            for peca in pecas:
                imprimir_peca(peca, print_fn)
                print_fn('-' * 15)
        elif opcao_consulta == 2:
            codigo = int(input_fn('Digite o código da peça: '))
            for peca in pecas:
                if peca['codigo'] == codigo:
                    imprimir_peca(peca, print_fn)
                    print_fn('-' * 15)
                    break
        elif opcao_consulta == 3:
            fabricante = input_fn('Digite o fabricante da peça: ')
            for peca in pecas:
                if peca['fabricante'] == fabricante:
                    imprimir_peca(peca, print_fn)
                    print_fn('-' * 15)
        elif opcao_consulta == 4:
            finaliza_consulta = True
            print_fn()
        else:
            print_fn('Opção inválida. Tente novamente!')


def obter_opcao_consulta(input_fn: Callable = input) -> int:
    return int(input_fn('Opção: '))


def remover_peca(input_fn: Callable = input, print_fn: Callable = print):
    print_fn('\nVocê selecionou a opção para remover uma peça')
    codigo = int(input_fn('Código da peça a ser removida: '))
    peca_remover = {}
    for peca in pecas:
        if peca['codigo'] == codigo:
            peca_remover = peca
            break

    pecas.remove(peca_remover)
    print_fn('Peça removida com sucesso')

# def remover_peca(input_fn=input, print_fn=print):
#     print_fn('\nVocê selecionou a opção para remover uma peça')
#     codigo = int(input_fn('Código da peça a ser removida: '))
#     peca_remover = next((peca for peca in pecas if peca['codigo'] == codigo), None)
#
#     if peca_remover:
#         pecas.remove(peca_remover)
#         print_fn('Peça removida com sucesso')
#     else:
#         print_fn('Código de peça não encontrado')


if __name__ == '__main__':
    opcao = 0
    while opcao != 4:
        print('Escolha a opção desejada: ')
        print('1 - Cadastrar Peças')
        print('2 - Consultar Peças')
        print('3 - Remover Peças')
        print('4 - Sair')
        opcao = int(input('Opção desejada: '))

        if opcao == 1:
            cadastrar_peca([])
        elif opcao == 2:
            consultar_pecas()
        elif opcao == 3:
            remover_peca()
        elif opcao > 4 or opcao < 1:
            print('Opção inválida')

    print('Obrigado por usar o nosso aplicativo!')
