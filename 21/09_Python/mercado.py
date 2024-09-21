estoque = {}

def main():
    while True:
        print("\nMercado Kipãozão")
        print("1 - Vender item")
        print("2 - Consultar estoque")
        print("3 - Registrar item")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            print(f"Todos os produtos do estoque: {list(estoque.keys())}")
            venda = input("Qual item deseja vender? ")
            
            if venda in estoque:
                quantidade_venda = int(input("Quantos itens deseja vender? "))
                if quantidade_venda <= int(estoque[venda]):
                    estoque[venda] = str(int(estoque[venda]) - quantidade_venda)
                    print(f"Venda realizada: {quantidade_venda} de {venda}.")
                else:
                    print("Quantidade em estoque insuficiente!")
            else:
                print("Item não encontrado no estoque.")
        
        elif escolha == "2":
            print("Estoque atual:")
            for item, quantidade in estoque.items():
                print(f"{item}: {quantidade} unidades")
        
        elif escolha == "3":
            while True:
                item = input("Digite o nome do item: ")
                quantidade = input("Digite a quantidade de itens: ")
                if item in estoque:
                    estoque[item] = str(int(estoque[item]) + int(quantidade))
                else:
                    estoque[item] = quantidade
                escolha2 = input("Deseja registrar novamente? S/N\n").upper()
                if escolha2 == "N":
                    break
        
        elif escolha == "4":
            print("Saindo do sistema. Até mais!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
