#Usei o tabulate para ciar e deixar a tabela mais bonita
#pip install tabulate
#https://pypi.org/project/tabulate/ 
import os
from tabulate import tabulate

def menu():  
  os.system('cls' if os.name == 'nt' else 'clear')
  print('\n..:: Menu da Loja ::..\n')
  print('1 - Registrar venda')
  print('2 - Repor estoque')
  print('3 - Mostrar estoque')
  print('4 - Mostrar compras')
  print('5 - Maior compra')
  print('9 - Sair\n')
  item = input('Escolha uma opção: ')
  return item

def registrar_venda():
    print('\n Registre uma compra')
    input('teste')
def repor_estoque():
    print('Certo')
def mostrar_estoque():
    estoque = [[1, "Calça", 20, "R$ 112,00"],
               [2, "Camisa", 18, "R$ 95,00"],
               [3, "Bermuda", 23, "R$ 49,90"],
               [4,"Saia",12,"R$ 169,00"],
               [5,"Blusa",9,"R$ 120,00"],
               [6,"Moletom",4,"R$ 135,00"],
               [7,"Meia",17,"R$ 12,99"],
               [8,"Tênis",8,"R$ 183,00"],
               [9,"Bota",3,"R$ 219,90"]]
    headers_tabela = ["Código", "Descrição", "Estoque", "Valor"]
    print(tabulate(estoque, headers=headers_tabela, tablefmt="grid")) 
def mostrar_compras():
    print('\n certo \n')
def maior_compra():
    print('certo')
if __name__ == '__main__':
    escolha = '0'
    while(escolha != '9'):
        escolha = menu()
        if escolha == '1':
            registrar_venda()
        elif escolha == '2':
            repor_estoque()
        elif escolha == '3':
            mostrar_estoque()
        elif escolha == '4':
            mostrar_compras()
        elif escolha == '5':
            maior_compra()
        elif escolha == '9':
            print('\nSaindo...\n')
        else:
            print('\nOpção desconhecida!\n')
        input('Pressione ENTER para continuar')
