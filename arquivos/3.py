"""
Modo de Atualização:
O modo "r+" abre o arquivo para leitura e escrita, mantendo o conteúdo existente. 
O modo "w+" abre o arquivo para leitura e escrita, excluindo o conteúdo anterior. 
O modo "a+" abre o arquivo para leitura e escrita, adicionando novo conteúdo ao final.
"""

arquivo = open("arquivo.txt", "r+")

conteudo_atual = arquivo.read()
print("Conteúdo atual:\n")
print(conteudo_atual) #1 2 3texto6 7 8

novo_conteudo = "Este é um novo conteúdo.\n"
arquivo.write(novo_conteudo)
print("Novo conteúdo escrito com sucesso!")


#movendo o ponteiro para o ínicio do arquivo, atualmente ele está no final do arquivo, já que eu escrevi nele e o ponteiro foi pulando de posição até chegar no final
arquivo.seek(0)

conteudo_atual = arquivo.read()
print(conteudo_atual)

arquivo.close()


