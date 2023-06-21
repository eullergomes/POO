"""
Implementar um algoritmo que modele a associação simples entre as classes Aluno e Curso. Cada aluno 
pode estar associado a apenas um curso, e cada curso pode ter vários alunos associados. O algoritmo deve
permitir a criação de alunos e cursos, associar um aluno a um curso específico e exibir os detalhes do
aluno e do curso ao final.
"""

class Curso:
    def __init__(self, nome: str, codigo: str):
        self.__nome = nome
        self.__codigo = codigo
        
    def informacoes_curso (self):
        print(f"Curso: {self.__nome}")
        print(f"Código: {self.__codigo}")
    
    @property
    def nome(self):
        return self.__nome

class Aluno:
    def __init__(self, nome: str, matricula: str):
        self.__nome = nome
        self.__matricula = matricula
        self.__curso = None

    def associar_curso(self, curso: Curso):
        self.__curso = curso

    def exibir_detalhes(self):
        print("Nome:", self.__nome)
        print("Matrícula:", self.__matricula)
        if self.curso:
            self.curso.informacoes_curso()
        else:
            print("Nenhum curso associado.")
            
    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula


#Criando objetos Aluno
aluno1 = Aluno("João", "123")
aluno2 = Aluno("Maria", "456")

# Criando objetos Curso
curso1 = Curso("Python para Iniciantes", "P101")
curso2 = Curso("Java Avançado", "J201")

# Associando alunos aos cursos
curso1.aluno = aluno1
curso2.aluno = aluno2

# Exibindo os detalhes dos alunos e cursos
print(f"Detalhes do Aluno {aluno1.nome}:")
print(f"Nome: {aluno1.nome}")
print(f"Matrícula: {aluno1.matricula}")
print(f"Curso Associado: {curso1.nome}\n")

print(f"Detalhes do Aluno {aluno2.nome}:")
print(f"Nome: {aluno2.nome}")
print(f"Matrícula: {aluno2.matricula}")
print(f"Curso Associado: {curso2.nome}")
