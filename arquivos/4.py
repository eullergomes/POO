arquivo = open("arquivo.txt", "w")
arquivo.write("1 2 3 4 5 6 7 8") #o espaço tbm conta 

arquivo.seek(5)

arquivo.write("texto")

arquivo.close()

