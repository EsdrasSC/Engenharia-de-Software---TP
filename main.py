from estacionamento import Estacionamento

def main():
    est = Estacionamento()

    while True:
        print("\n--- Sistema PARKSYNC ---")
        est.mostrar_status()
        print("\nDigite o número da vaga para alterar (1-4) ou 0 para sair:")
        opc = int(input("> "))
        if opc == 0:
            break

        print("Digite o novo estado (livre / ocupada / reservada):")
        estado = input("> ").lower()
        est.alterar_estado(opc, estado)

if __name__ == "__main__":
    main()
