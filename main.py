from classificador import ClassificadorPlantas


def mostrar_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Classificar uma Planta")
    print("2 - Listar Grupos e Plantas Identificáveis pelo Sistema")
    print("0 - Sair")


def main():
    classificador = ClassificadorPlantas()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            classificador.classificar()
        elif opcao == "2":
            classificador.listar_grupos()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()