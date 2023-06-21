#else é executado quando nenhum erro (except) for encontrado

try:
    # Código que pode gerar exceções
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
else:
    print("Conteúdo do arquivo:")
    print(conteudo)