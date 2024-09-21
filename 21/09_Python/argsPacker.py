def nome_completo(*nomes):
    nome_completo = ""
    for nome in nomes:
        nome_completo += nome + " "
    return nome_completo

print(nome_completo('Ana', 'Silva', 'do', 'Santos'))