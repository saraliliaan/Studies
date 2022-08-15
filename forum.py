#print('01 Reutilização do código – Funções e Módulos - cap. 4 - Use a Cabeça! Python (anexo)', end='')
#print('\nAtividade:')
#print('(a) Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.')

#Tabuada = int(input('Digite um número para imprimir a sua Tabuada: '))
#print('{} X {:2} = {}'.format(Tabuada, 1, Tabuada*1))
#print('{} X {:2} = {}'.format(Tabuada, 2, Tabuada*2))
#print('{} X {:2} = {}'.format(Tabuada, 3, Tabuada*3))
#print('{} X {:2} = {}'.format(Tabuada, 4, Tabuada*4))
#print('{} X {:2} = {}'.format(Tabuada, 5, Tabuada*5))
#print('{} X {:2} = {}'.format(Tabuada, 6, Tabuada*6))
#print('{} X {:2} = {}'.format(Tabuada, 7, Tabuada*7))
#print('{} X {:2} = {}'.format(Tabuada, 8, Tabuada*8))
#print('{} X {:2} = {}'.format(Tabuada, 9, Tabuada*9))
#print('{} X {} = {}'.format(Tabuada, 10, Tabuada*10))



#exercicio b
#from random import sample

#Nome = input('Digite uma palavra: ').upper()
#Embaralha = sample(Nome, len(Nome))
#print(f"{Embaralha}")


#outra versao da atividade A
numero = int(input('Digite um número: '))

for x in range(1,11):
    print(f"{numero} x {x} = {numero * x}")