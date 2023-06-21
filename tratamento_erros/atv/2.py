#Crie uma função em Python que receba o tamanaho de uma lista e os valores dela e retorne a média aritmética dos elementos. Certifique-se de lidar com exceções caso a lista esteja vazia ou contenha valores não numéricos.

def lista_media():
    try:
        tam = int(input("Digite o tamanho da lista: "))
        lista = []
        
        if tam == 0:
            raise ValueError("Lista vazia")
    
        for i in range(tam):
            num = float(input(f"Digite um número para o indice {i}: "))
            lista.append(num)
        
        media = sum(lista) / len(lista)
        
        return media
            
    except ValueError as e:
        print(f"Ocorreu um ValueError: {str(e)}")
    except TypeError:
        print(f"Ocorreu um TypeError: {str(e)}")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
        
        
media = lista_media()

if media is not None:
    print(f"\nMédia = {media}\n")