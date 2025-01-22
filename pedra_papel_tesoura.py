import random

def jogada(palpite):

    opcao = [

    # Pedra
    """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """ ,

    # Papel
    """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """ ,

    # Tesoura
    """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """


    ]

    return (opcao[palpite])

def jogada_usuario(opcao):
    
    try:
        opcao = int(opcao)
        if 0 <= opcao <= 2:
            print(f"Sua jogada: ") 
            return jogada(opcao)
        else:
            print("\nOpção inválida! Escolha 0, 1 ou 2.")
            return None

    except ValueError:
        print("\nPor favor, digite apenas números!")
        return None
    
def jogada_computador():
    opcao_pc = random.randint(0, 2)
    print("A jogada do computador foi: ")
    return jogada(opcao_pc), opcao_pc

def verificar_vencedor():
    

def main():
    while True:
        print("\nBem-vindo ao jogo de Pedra, Papel e Tesoura!")
        print("Selecione uma das opções:")
        print("0. Pedra")
        print("1. Papel")
        print("2. Tesoura")
        print("3. Sair")

        opcao = input("\nEscolha uma opção (0-3): ")

        if opcao == '3':
            print("Obrigado por jogar!")
            break

        jogada_player = jogada_usuario(opcao)
        if jogada_player is None:
            continue

        print(jogada_player)
        jogada_visual_pc, numero_jogada_pc = jogada_computador()
        print(jogada_visual_pc)
        print("\nGostaria de jogar novamente?")
        sair = input("\nEscolha sua opção, '1' para continuar e '0' para sair: ")
        if sair == '0':
            print("Muito obrigado por jogar!")
            break
        else:
            continue

if __name__ == "__main__":
    main()
