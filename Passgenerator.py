import argparse
import random
import sys
from caracteres import *



#Loop que deleta os tipos passados ex: 1 = especiais
#ele removerá os caracteres especiais
def loopDeletarTipoDeString(tipoDeString,numerosAdeletar):
  for i in numerosAdeletar:
    tipoDeString.remove(i)




    
#Define os paramentros do sistema
def parametros():
  parser = argparse.ArgumentParser(prog="Gerador de senha")

  parser.add_argument("-q", "--quantidade", help="Quantidade de caracteres pra senha")
  parser.add_argument("-n", "--numeros",action='store_true', help="Senha terá apenas numeros")
  parser.add_argument("-l", "--letras",action='store_true', help="Senha terá apenas letras")
  parser.add_argument("-e", "--especiais",action='store_true', help="Senha terá apenas especiais")
  parser.add_argument("-z", "--zeroespeciais",action='store_true', help="Senha não terá especiais")

  arg = parser.parse_args()    
  return arg



#Dependendo de qual paramentro o usuario passou ele exclui os caracteres 
def escolhas(arg, tipoDeString):
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



#Junta a lista senha e printa
def JuntaSenha(senha):
  senhaJuntada = "".join(senha)
  print(senhaJuntada)



#Checa se mais de um parametro foi passado
def CheckParametros(arg):
  selected = sum([arg.numeros,arg.letras,arg.especiais,arg.zeroespeciais])
  
  if selected > 1:
      print("Foi definido mais de um parametro")
      print("Use o seguinte comando para ver o help:\n$ python Passgenerator.py -h")
      sys.exit()


#Gera a senha
def GenSenha(arg,senha,tipoDeString):
  
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

#Chuta pra que ele serve XD
def ValidarTipoDoParametro(arg):
    if arg.quantidade is None or not arg.quantidade.isdigit():
      print("parametro passado invalido")
      print("Use o seguinte comando para ver o help:\n$ python Passgenerator.py -h")
      sys.exit()

#Função Main
def main():
  
  arg = parametros()
  tipoDeString = [1,2,3,4]
  senha = []
  
  ValidarTipoDoParametro(arg)

  CheckParametros(arg)
  
  escolhas(arg, tipoDeString)

  GenSenha(arg,senha,tipoDeString)

  JuntaSenha(senha)

main()
  
  # te amo celo atenciosamente nami :3 <3