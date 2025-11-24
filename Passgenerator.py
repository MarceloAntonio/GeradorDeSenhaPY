import argparse
import random

def loopDeletarTipoDeString(tipoDeString,numerosAdeletar):
  for i in numerosAdeletar:
    tipoDeString.remove(i)


def main():

  parser = argparse.ArgumentParser(prog="Gerador de senha")

  parser.add_argument("-q", "--quantidade", help="Quantidade de caracteres pra senha")
  parser.add_argument("-n", "--numeros",action='store_true', help="Senha terá apenas numeros")
  parser.add_argument("-l", "--letras",action='store_true', help="Senha terá apenas letras")
  parser.add_argument("-e", "--especiais",action='store_true', help="Senha terá apenas especiais")
  parser.add_argument("-z", "--zeroespeciais",action='store_true', help="Senha não terá especiais")

  
  arg = parser.parse_args()

  especiais = [ '.', '+', '-', '@', '#', '*', '!', '?', '~']
  numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  letras_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  letras_mai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  selected = sum([arg.numeros,arg.letras,arg.especiais,arg.zeroespeciais])
  if selected > 1:
      print("Só pode escolher um")
      return

  tipoDeString = [1,2,3,4]
  senha = []

  #te amo nami - te amo celo atenciosamente nami :3 <3
  if arg.numeros:
    numerosAdeletar = [1,3,4]
    loopDeletarTipoDeString(tipoDeString,numerosAdeletar)
  if arg.letras:
    numerosAdeletar = [1,2]
    loopDeletarTipoDeString(tipoDeString,numerosAdeletar)
  if arg.especiais:
    numerosAdeletar = [2,3,4]
    loopDeletarTipoDeString(tipoDeString,numerosAdeletar)
  if arg.zeroespeciais:
    numerosAdeletar = [1]
    loopDeletarTipoDeString(tipoDeString,numerosAdeletar)



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
  
main()
  