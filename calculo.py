#a = float(input("Digite um valor para a: "))
#b = float(input("Digite um valor para b: "))
#if a > b: 
#    print ("a é maior que b")
#else:
#    print("b é maior que a")

qtd_faltas = int(input("Digite o número de faltas: "))
med_final = float(input("Digite a média final: "))

if qtd_faltas <= 5 and med_final >= 7:
    print ("Aluno Aprovado! Parabéns.")
else:
    print("Aluno reprovado.")
    