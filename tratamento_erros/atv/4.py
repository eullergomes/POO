#Desenvolva um programa de jogo de adivinhação em Python. O programa deve gerar um número aleatório e solicitar ao usuário que adivinhe esse número. O programa deve lidar com exceções caso o usuário insira uma entrada inválida, como uma string em vez de um número, e fornecer dicas ao usuário para ajudar na adivinhação(por ex. " o numero que vc digitou é maior" ou "o numero que vc digitou é menor").

import random

def menu():
    print("MENU:")
    print("1. Começar")
    print("0. Sair")
    print("\nInforme a opção: ")


def sortear_num():
    x = random.randint(1,52)
    print("\nNúmero sorteado")
    return x

while True:
    try:
        menu()
        opc = int(input())
    
        match opc:
            case 1:
                x = sortear_num()
        
                while True:
                    num = int(input("Informe um número: "))
            
                    if num == x:
                        print("\nACERTOU\n")
                        break
                    elif num > x:
                        print("\nO numero que vc digitou é MAIOR\n")
                    elif num < x:
                        print("\nO numero que vc digitou é MENOR\n")
                    else:
                        print("\nERROU\n")
                        print("Tente novamente")
            case 0:
                print("\nEncerrando...\n")
                break
            
            case _:
                print("\nOperação inválida\n");
    
    except ValueError:
        print(f"\nErro: você digitou algo inválido\n")
        print("Tente novamente:")