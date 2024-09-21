def meu_decorador(funcao):
    def funcao_decorada():
        print("Antes da função ser chamada.")
        funcao()
        print("Depois da função ser chamada.")
    return funcao_decorada

@meu_decorador
def minha_funcao():
    print("Olá, mundo!")

minha_funcao()