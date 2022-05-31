from funcoes import *

opcao = 0

while opcao not in (1, 2, 3):
    apresentar_opcoes()
    opcao = int(input('---> '))
    valida_opcoes(opcao)

opcoes(opcao)