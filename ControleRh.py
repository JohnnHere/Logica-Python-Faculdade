print("Bem vindo ao programa de controle de funcionários da Orlando Produções - João Orlando Ferreira Junior")

#Aqui eu estou instanciando uma lita vazia de funcionários, para que eu possa poupular a mesma como eu bem entender.
#E também um contador iniciado em 1 para garantir que os ids sejam únicos e sequenciais.
funcionarios = []
contador = 1

#Função para cadastrar funcionários, com variáveis sendo instanciadas para dar características a este funcionário.
#O .append é utilizado para adicionar o funcionário na lista.
def cadastrar_funcionario(id):
  nome = input("Insira o nome do funcionário: ")
  setor = input("Insira o setor do funcionário: ")
  salario = input("Insira o salário do funcionário: ")
  funcionario = {"id": id, "nome": nome, "setor": setor, "salario": salario}
  funcionarios.append(funcionario)

#Função para cosultar funcionários, com opção de consulta por id, consultar todos, consultar todos e
def consultar_funcionarios():
      opcao = input(
          "1) Consultar Todos os Funcionários  2) Consultar Funcionário por Id  3) Consultar Funcionário(s) por Setor  "
          "4) Retornar  Insira a opção desejada: ")

      if opcao == "1":
          for funcionario in funcionarios:
              print("Funcionário:", funcionario["nome"])
              print("Setor:", funcionario["setor"])
              print("Salário:", funcionario["salario"])
              print()
      elif opcao == "2":
          id = int(input("Insira o id do funcionário que deseja consultar: "))
          for funcionario in funcionarios:
              if funcionario["id"] == id:
                  print("Funcionário:", funcionario["nome"])
                  print("Setor:", funcionario["setor"])
                  print("Salário:", funcionario["salario"])
                  print()
      elif opcao == "3":
          setor = input("Insira o setor que deseja consultar: ")
          for funcionario in funcionarios:
              if funcionario["setor"] == setor:
                  print("Funcionário:", funcionario["nome"])
                  print("Setor:", funcionario["setor"])
                  print("Salário:", funcionario["salario"])
                  print()
      else:
          return

#Função para remover funcionários a partir do seu id. Aqui se utiliza um for loop para encontrar o funcionário correto na
#lista de funcionários. o .remove remove ele assim que o mesmo é identificado pelo seu id. Caso o id seja inexistente,
#não há o que deletar, portanto uma mensagem de 'não encontrado' é printada.
def remover_funcionario():
  id = int(input("Insira o código do funcionário que deseja remover: "))
  for funcionario in funcionarios:
    if funcionario["id"] == id:
      funcionarios.remove(funcionario)
      print("Funcionário removido com sucesso.")
      return
  print("Funcionário não encontrado.")


# Cadastrando um funcionário
cadastrar_funcionario(1)

# Cadastrando um funcionário
cadastrar_funcionario(2)

# Cadastrando um funcionário
cadastrar_funcionario(3)

# Consultando os funcionários
consultar_funcionarios()

# Removendo um funcionário
remover_funcionario()

# Consultando os funcionários novamente
consultar_funcionarios()