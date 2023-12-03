print("1 - soma")
print("2 - multiplicacao")
print("3 - subtracao")
print("4 - divisao\n")

resposta = int(input("digite o numero de uma opcao:\n"))

if (resposta == 1):
  n1 = float(input("\nnumero 1: "))
  n2 = float(input("numero 2: "))
  resultado = n1 + n2 
  print("\nresultado:",resultado)

if (resposta == 2):
  n1 = float(input("\nnumero 1: "))
  n2 = float(input("numero 2: "))
  resultado = n1 * n2 
  print("\nresultado:",resultado)

if (resposta == 3):
  n1 = float(input("\nnumero 1: "))
  n2 = float(input("numero 2: "))
  resultado = n1 - n2 
  print("\nresultado:",resultado)

if (resposta == 4):
  n1 = float(input("\nnumero 1: "))
  n2 = float(input("numero 2: "))
  resultado = n1/n2 
  print("\nresultado:",resultado)


def soma(entrada1,entrada2):
  saida = entrada1 + entrada2
  return saida

def multiplicacao(entrada1,entrada2):
  saida = entrada1 * entrada2
  return saida

print("\n\nOutra calculadora")
n1 = int(input("numero1: "))
n2 = int(input("numero2: "))

print("\n1 - soma")
print("2 - multiplicacao")

opcao = int(input("\ndigite o numero de uma opcao: "))

if opcao == 1:
  resultado = soma(n1,n2)
if opcao == 2:
  resultado = multiplicacao(n1,n2)
  
print("\nresultado =",resultado)
  

  
