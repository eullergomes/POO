arquivo = open("arquivo.txt", "w")
lista = ["Maria\n", "Julia\n", "Feia\n"]
arquivo.writelines(lista)
arquivo.close()

arquivo = open("arquivo.txt", "r")

print(arquivo.read())

arquivo.close()