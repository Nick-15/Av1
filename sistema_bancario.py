users = {'nick': {'balanco': 250.0}, 'gus': {'balanco': 500.0}} #Dicionário responsável por armazenar os usuários previamente cadastrados

def deposito(usuario): #Função responsáve pelo depósito
  saldo = float(input("Entre o valor do deposito R$")) #'Saldo' váriavel float responsável por atualizar o 'balanco' no dicionário 'users'
  if saldo > 0: #Se for maior que '0'...
    users[usuario]["balanco"] += saldo #...Adciona ao dicionário a váriavel 'saldo' dentro de um 'balanco' individual de cada usuário
    print("Deposito feito com sucesso!") #Print <3
  else: #caso sejá outra coisa...
    print("Impossivel depositar um valor negativo") #...Print <3

def saque(usuario): #Função responsáve pelo saque
  saldo = float(input("Entre o valor do saque R$")) #'Saldo' váriavel float responsável por atualizar o 'balanco' no dicionário 'users'
  if saldo > users[usuario]["balanco"]: #Se o saque for maior que o 'balanco' individual de cada usuário...
    print("Saldo insuficiente!") #...Saque invalido
    print(f"Seu saldo é R${users[usuario]['balanco']}") #Print do usuário e o seu balanço
  elif saldo > 0: #Se 'saldo' for maior que '0'...
    users[usuario]["balanco"] -= saldo #Atualiza o 'balanco' do usuário
    print("Saque feito com sucesso!") #...Saque realizado com sucesso
  else: #Caso seja outra coisa...
    print("Impossivel sacar um valor negativo") #...Print <3

def consulta(usuario): #Função responsáve pela consulta
  print(f"Seu saldo é R${users[usuario]['balanco']}") #Print do usuário e o seu balanço

def main(): #Função responsáve pelo uso do sistema
  usuario = input("Bem vindo ao seu Banco, entre o titular da conta: ") #variável do usuário
  print("Bem vindo a sua Conta Bancária", usuario) #Print <3
  if usuario not in users: #Se a váriavel 'usuario' não estiver no dicionário 'users'...
    print("Nova conta registrada") #Print <3
    users[usuario] = {"balanco": 0} #Atualiza o valor do 'balanco' para '0'

  while True: #Repetição
    try: #Função que permite textar um bloco de código sobre erros
      esc = input("Escolha uma ação (Deposito = 1, Saque = 2, Consulta = 3, Sair = 4): ") #Váriavel responsavel pela escolha do usuário
      if esc == "1": #Se 'esc' == '1'...
        deposito(usuario) #...Chama função 'deposito' com o nome do usuário
      elif esc == "2": #Se 'esc' == '2'...
        saque(usuario) #...Chama função 'saque' com o nome do usuário
      elif esc == "3": #Se 'esc' == '3'...
        consulta(usuario) #...Chama função 'consulta' com o nome do usuário
      elif esc == "4": #Se 'esc' == '4'...
        print("Obrigado pela preferencia :D") #Print <3
        break #Finaliza o sistema
      else: #Se não for escolhido nenhuma das opções...
        print("Operação invalida") #...Print <3
    except ValueError: #Se houver um erro nos valores...
      print("Valor inválido") #...Print <3

main() #Chama a função 'main'
