#def executar_insertion_sort(lista):
#    n = len(lista)
#    for i in range (1, n):
#        valor_inserir = lista[i]
#        j = i - 1
#        
#        while j >= 0 and lista[j] > valor_inserir:
#            lista[j + 1] = lista[j]
#            j -= 1
#        lista[j + 1] = valor_inserir
#    
#    return lista

#lista = [10, 8, 7, 3, 2, 1]
#executar_insertion_sort(lista)
#print(lista)

#def executar_selection_sort(lista):
#    n = len(lista)
#    
#    for i in range(0, n-1):
#        min = i
#        for j in range(i+1, n):
#            if lista[j] < lista[min]:
#                min = j
#        lista[i], lista[min] = lista[min], lista[i]
#    return lista
#
#lista = [10, 8, 7, 3, 2, 1]
#executar_selection_sort(lista)
#print(lista)

def executar_bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = [10, 8, 7, 3, 2, 1]
executar_bubble_sort(lista)
print(lista)