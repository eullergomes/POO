"""
Descrição do exemplo: Vamos modelar a associação entre uma empresa, seus departamentos, funcionários e projetos.
Cada empresa pode ter vários departamentos, cada departamento pode ter vários funcionários e cada projeto pode estar associado a
um departamento específico. O algoritmo deve permitir cadastrar empresas, departamentos, funcionários e projetos, e exibir os
detalhes de cada um.
"""

class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.__nome = nome
        self.__salario = salario
        
    def informacoes_funcionario(self):
        print(f"Nome: {self.__nome}\nSalário: {self.__salario}")

class Projeto:
    def __init__(self, nome: str, descricao: str):
        self.__nome = nome
        self.__descricao = descricao
        
    def informacoes_proj(self):
        print(f"Nome: {self.__nome}\nDescrição: {self.__descricao}")

class Departamento:
    def __init__(self, nome: str, descricao: str):
        self.__nome = nome
        self.__descricao = descricao
        self.__funcionarios = []
        self.__projeto = ''
        
    def adicionar_funcionario(self, funcionario: Funcionario):
        self.__funcionarios.append(funcionario)
        
    def listar_funcionarios(self):
        for funcionario in self.__funcionarios:
            funcionario.informacoes_funcionario()
            print()
    
    def definir_projeto(self, projeto: Projeto):
        self.__projeto = projeto
        
    def informacoes_departamento(self):
        print(f"Nome: {self.__nome}")
        print(f"Descrição: {self.__descricao}")
        print(f"Projeto:\n")
        projeto.informacoes_proj()

class Empresa:
    def __init__(self, nome: str, endereco: str):
        self.__nome = nome
        self.__endereco = endereco
        self.__departamentos = []
        
    def adicionar_departamento(self, departamento: Departamento):
        self.__departamentos.append(departamento)
    
    def listar_departamentos(self):
        print("Departamentos da Empresa:")
        for departamento in self.__departamentos:
            departamento.informacoes_departamento()
            
    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco
        
        
# Criando uma empresa
empresa = Empresa("Minha Empresa", "Rua Principal, 123")

# Criando departamentos
departamento1 = Departamento("Vendas", "Departamento de vendas")
departamento2 = Departamento("RH", "Departamento de recursos humanos")

# Adicionando departamentos à empresa
empresa.adicionar_departamento(departamento1)
empresa.adicionar_departamento(departamento2)

# Criando funcionários
funcionario1 = Funcionario("João", 3000.0)
funcionario2 = Funcionario("Maria", 4000.0)

# Adicionando funcionários aos departamentos
departamento1.adicionar_funcionario(funcionario1)
departamento1.adicionar_funcionario(funcionario2)

# Criando um projeto
projeto = Projeto("Projeto A", "Projeto de desenvolvimento de software")

# Definindo projeto no departamento
departamento1.definir_projeto(projeto)
departamento1.informacoes_departamento()

# Exibindo os detalhes da empresa, departamentos e funcionários
empresa.listar_departamentos()
print("Funcionários do Departamento Vendas:")
departamento1.listar_funcionarios()
