# Cria um novo arquivo chamado "arquivo.txt" para escrita
arquivo = open("arquivo.txt", "w")

# Escreve conteúdo no arquivo
arquivo.write("Olá, mundo!")

# Fecha o arquivo
arquivo.close()


#imprimindo o arquivo
arquivo = open("arquivo.txt", "r")

print(arquivo.read())

arquivo.close()
