import Prova1 as p1

def menu():
    print("\n--- Menu ---")
    print("1. Inserir personagem")
    print("2. Listar personagens")
    print("3. Atualizar personagem por ID")
    print("4. Atualizar personagens por filiação")
    print("5. Atualizar personagens por moralidade")
    print("6. Atualizar personagens por ranque")
    print("7. Excluir personagem por ID")
    print("8. Excluir personagens por filiação")
    print("9. Excluir personagens por moralidade")
    print("10. Sair")

def obter_dados_personagem():
    nome = input("Nome: ")
    classe = input("Classe: ")
    ranque = input("Ranque: ")
    arma = input("Arma: ")
    filiacao = input("Filiação: ")
    moralidade = input("Moralidade: ")
    return nome,classe,ranque,arma,filiacao, moralidade

if __name__ == "__main__":
    p1.iniciar_banco()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Inserir Personagem ---")
            dados = obter_dados_personagem()
            p1.inserir_personagem(*dados)

        elif opcao == "2":
            print("\n--- Lista de Personagens ---")
            p1.listar_personagens()

        elif opcao == "3":
            print("\n--- Atualizar por ID ---")
            id_personagem = int(input("ID do personagem: "))
            dados = obter_dados_personagem()
            p1.atualizar_personagem_por_id(id_personagem, *dados)

        elif opcao == "4":
            print("\n--- Atualizar por Filiação ---")
            filiacao_antiga = input("Filiação atual: ")
            dados = obter_dados_personagem()
            p1.atualizar_personagens_por_filiacao(filiacao_antiga, *dados)

        elif opcao == "5":
            print("\n--- Atualizar por Moralidade ---")
            moralidade = input("Moralidade: ")
            p1.atualizar_personagem_por_moralidade(moralidade)

        elif opcao == "6":
            print("\n--- Atualizar por Ranque ---")
            ranque = input("Ranque: ")
            p1.atualizar_personagem_por_ranque(ranque)

        elif opcao == "7":
            print("\n--- Excluir por ID ---")
            id_personagem = int(input("ID do personagem: "))
            p1.excluir_personagem_por_id(id_personagem)

        elif opcao == "8":
            print("\n--- Excluir por Filiação ---")
            filiacao = input("Filiação: ")
            p1.excluir_personagens_por_filiacao(filiacao)

        elif opcao == "9":
            print("\n--- Excluir por Moralidade ---")
            moralidade = input("Moralidade: ")
            p1.excluir_personagens_por_moralidade(moralidade)

        elif opcao == "10":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

