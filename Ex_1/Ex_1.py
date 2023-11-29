def calcular_valor(valor_unitario, quantidade):
    desconto = 1

    if 10 <= quantidade <= 99:
        desconto = 0.95
    elif 100 <= quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85

    valor_com_desconto = valor_unitario * desconto * quantidade
    valor_sem_desconto = valor_unitario * quantidade

    return valor_com_desconto, valor_sem_desconto
