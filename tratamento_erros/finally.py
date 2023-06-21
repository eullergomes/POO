#finally é usado para definir um código que será executado sempre, independentemente de ocorrer uma
#exceção ou não. O bloco finally é útil para realizar ações de limpeza, como fechar arquivos ou liberar 
#recursos, garantindo que essas ações sejam realizadas mesmo que uma exceção seja lançada.

try:
    # Código que pode gerar exceções
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.write("texto aqui")
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
finally:
    arquivo.close()
    print("Fechando o arquivo.")