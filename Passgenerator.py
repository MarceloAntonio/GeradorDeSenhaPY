import argparse
import random

parser = argparse.ArgumentParser(prog="Gerador de senha")

parser.add_argument("-q", "--quantidade", help="Quantidade de caracteres pra senha")

arg = parser.parse_args()

especiais = [ '.', '+', '-', '@', '#', '*', '!', '?', '~']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letras_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letras_mai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


tipoDeString = [1,2,3,4]
senha = []

#te amo nami - te amo celo atenciosamente nami :3 <3

if arg.quantidade:
  while len(senha) < int(arg.quantidade):
    
    escolha = random.choice(tipoDeString)
    if escolha == 1:
      senha.append(random.choice(especiais))
    elif escolha == 2:
      senha.append(random.choice(numeros))
    elif escolha == 3:
      senha.append(random.choice(letras_min))
    elif escolha == 4:
      senha.append(random.choice(letras_mai))

  

senhaJuntada = "".join(senha)
print(senhaJuntada)
  
  
  