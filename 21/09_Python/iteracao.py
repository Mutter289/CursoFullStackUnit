lista = []
for i in range(0,101):
    lista.append(i)
print(lista[10:21:])
print(lista[19::-1])
print([x for x in lista[80:91] if x%2 == 0])