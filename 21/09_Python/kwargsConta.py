def valor_conta(**produtos):
    valor = 0
    for produto, preco in produtos.items():
        valor += preco
    return valor

total = valor_conta(carne=50, cerveja=8)
print(f"O valor total da conta é: {total}")
