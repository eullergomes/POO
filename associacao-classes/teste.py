class Cliente:
  def __init__(self, nome: str, endereco: str, telefone: int, email: str):
    self.nome = nome
    self.endereco = endereco
    self.telefone = telefone
    self.email = email
    self.pedidos = []

def check_dados_cliente(nome: str, telefone: str, email: str, enderecos):
    if not nome.strip() or not telefone.strip() or not email or not enderecos.strip():
        raise ValueError("Ausencia de dado(s)")

def novo_cliente():
  print(" - Novo cliente - ")
  nome = input("Nome: ")
  telefone = input("Telefone: ")
  email = input("E-mail: ")
  enderecos = []
  
  qtd = int(input("Digite a quantidade de endereços: ")) 
  if qtd <= 0:
    print("\nErro: cliente sem endereço")
    return
    
  for i in range(qtd):
    print(f"\nEndereço - {i + 1}")
    rua = input("Rua: ")
    try:
      n = int(input("Número: "))
      bairro = input("Bairro: ")

      endereco = {"rua": rua, "n": n, "bairro": bairro}

      check_dados_cliente(nome, telefone, email, enderecos)
      
      enderecos.append(endereco)
      
    except ValueError as erro:
      print(f"Erro: {erro}")

    else:
      print("- Cliente cadastrado - ")
    
      return Cliente(nome, endereco, telefone, email)
  
joao = novo_cliente()

print(joao.nome)
print(joao.telefone)
